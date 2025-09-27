"""Module providing async functions which return async generators containing trades realtime data."""

import asyncio
import logging
import signal
import types
from typing import Any, AsyncGenerator, List, Optional

from tvkit.api.chart.models.ohlcv import (
    OHLCVBar,
    OHLCVResponse,
    QuoteCompletedMessage,
    QuoteSymbolData,
    TimescaleUpdateResponse,
    WebSocketMessage,
)
from tvkit.api.chart.services import ConnectionService, MessageService
from tvkit.api.chart.utils import validate_interval
from tvkit.api.utils import validate_symbols, convert_symbol_format

# Configure logging
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s"
)


class OHLCV:
    """
    A real-time data streaming client for TradingView WebSocket API.

    This class provides async generators for streaming live market data including
    OHLCV bars, quote data, and trade information from TradingView.
    """

    def __init__(self) -> None:
        """
        Initializes the OHLCV class, setting up WebSocket connection parameters
        and request headers for TradingView data streaming.
        """
        self.ws_url: str = (
            "wss://data.tradingview.com/socket.io/websocket?from=chart%2F"
        )
        self.connection_service: Optional[ConnectionService] = None
        self.message_service: Optional[MessageService] = None

    async def __aenter__(self) -> "OHLCV":
        """Async context manager entry."""
        return self

    async def __aexit__(
        self,
        exc_type: Optional[type],
        exc_val: Optional[BaseException],
        exc_tb: Optional[types.TracebackType],
    ) -> None:
        """Async context manager exit."""
        if self.connection_service:
            await self.connection_service.close()

    async def _setup_services(self) -> None:
        """Initialize and connect the services."""
        self.connection_service = ConnectionService(self.ws_url)
        await self.connection_service.connect()
        self.message_service = MessageService(self.connection_service.ws)

    async def get_ohlcv(
        self, exchange_symbol: str, interval: str = "1", bars_count: int = 10
    ) -> AsyncGenerator[OHLCVBar, None]:
        """
        Returns an async generator that yields OHLC data for a specified symbol in real-time.

        This is the primary method for streaming structured OHLCV data from TradingView.
        Each yielded bar contains open, high, low, close, volume, and timestamp information.
        Symbols are automatically converted from EXCHANGE-SYMBOL to EXCHANGE:SYMBOL format.

        Args:
            exchange_symbol: The symbol in 'EXCHANGE:SYMBOL' or 'EXCHANGE-SYMBOL' format (e.g., 'BINANCE:BTCUSDT' or 'USI-PCC').
            interval: The interval for the chart (default is "1" for 1 minute).
            bars_count: The number of bars to fetch (default is 10).

        Returns:
            An async generator yielding structured OHLCV data as OHLCVBar objects.

        Raises:
            ValueError: If the symbol format is invalid
            WebSocketException: If connection or streaming fails

        Example:
            >>> async with OHLCV() as client:
            ...     async for bar in client.get_ohlcv("BINANCE:BTCUSDT", interval="5"):
            ...         print(f"Close: ${bar.close}, Volume: {bar.volume}")
        """
        await validate_symbols(exchange_symbol)
        # Convert symbol format from EXCHANGE-SYMBOL to EXCHANGE:SYMBOL if needed
        symbol_result = convert_symbol_format(exchange_symbol)
        converted_symbol: str = symbol_result.converted_symbol  # type: ignore
        validate_interval(interval)
        await self._setup_services()

        if not self.connection_service or not self.message_service:
            raise RuntimeError("Services not properly initialized")

        quote_session: str = self.message_service.generate_session(prefix="qs_")
        chart_session: str = self.message_service.generate_session(prefix="cs_")
        logging.info(
            f"Quote session generated: {quote_session}, Chart session generated: {chart_session}"
        )

        send_message_func = self.message_service.get_send_message_callable()
        await self.connection_service.initialize_sessions(
            quote_session, chart_session, send_message_func
        )
        await self.connection_service.add_symbol_to_sessions(
            quote_session,
            chart_session,
            converted_symbol,
            interval,
            bars_count,
            send_message_func,
        )

        async for data in self.connection_service.get_data_stream():
            # Try to parse different message types
            try:
                # Parse as generic WebSocket message first to check type
                message: WebSocketMessage = WebSocketMessage.model_validate(data)
                message_type: str = message.message_type

                logging.debug(f"Received message type: {message_type}")

                if message_type == "du":
                    # Try to parse as OHLCV data update
                    try:
                        ohlcv_response: OHLCVResponse = OHLCVResponse.model_validate(
                            data
                        )
                        # Yield all OHLCV bars from the response
                        for ohlcv_bar in ohlcv_response.ohlcv_bars:
                            yield ohlcv_bar
                    except Exception as e:
                        logging.debug(f"Failed to parse 'du' message as OHLCV: {e}")
                        continue

                elif message_type == "timescale_update":
                    # Try to parse as timescale update (historical OHLCV data)
                    try:
                        timescale_response: TimescaleUpdateResponse = (
                            TimescaleUpdateResponse.model_validate(data)
                        )
                        # Yield all OHLCV bars from the response
                        logging.info(
                            f"Received {len(timescale_response.ohlcv_bars)} OHLCV bars from timescale update"
                        )
                        for ohlcv_bar in timescale_response.ohlcv_bars:
                            yield ohlcv_bar
                    except Exception as e:
                        logging.debug(
                            f"Failed to parse 'timescale_update' message as OHLCV: {e}"
                        )
                        continue

                elif message_type == "qsd":
                    # Quote symbol data - contains current price info
                    try:
                        quote_data: QuoteSymbolData = QuoteSymbolData.model_validate(
                            data
                        )
                        current_price: Optional[float] = quote_data.current_price
                        if current_price is not None:
                            logging.info(
                                f"Quote data for {converted_symbol}: Current price = ${current_price}"
                            )
                        logging.debug(f"Quote symbol data: {quote_data.symbol_info}")
                    except Exception as e:
                        logging.debug(f"Failed to parse 'qsd' message: {e}")
                    continue

                elif message_type == "quote_completed":
                    # Quote setup completed
                    try:
                        quote_completed: QuoteCompletedMessage = (
                            QuoteCompletedMessage.model_validate(data)
                        )
                        logging.info(
                            f"Quote setup completed for symbol: {quote_completed.symbol}"
                        )
                    except Exception as e:
                        logging.debug(f"Failed to parse 'quote_completed' message: {e}")
                    continue

                elif message_type == "series_loading":
                    # Series loading message - continue waiting for data
                    logging.debug("Series loading for real-time data stream")
                    continue

                elif message_type == "study_loading":
                    # Study loading message - continue waiting for data
                    logging.debug("Study loading for real-time data stream")
                    continue

                elif message_type == "series_completed":
                    # Series completed message - continue waiting for data
                    logging.debug("Series completed for real-time data stream")
                    continue

                elif message_type == "study_completed":
                    # Study completed message - continue waiting for data
                    logging.debug("Study completed for real-time data stream")
                    continue

                elif message_type == "series_error":
                    # Series error - invalid interval or bars count
                    logging.error("Series error received from TradingView")
                    logging.error(f"Error details: {data}")
                    logging.error(
                        "Please check the interval - this timeframe may not be supported for the symbol"
                    )
                    logging.error("Also verify that bars_count is within valid range")

                    # Close connection and raise error
                    if self.connection_service:
                        await self.connection_service.close()

                    raise ValueError(
                        "TradingView series error: Invalid interval or bars count. "
                        "Please check that the timeframe is supported for this symbol "
                        "and that bars_count is within valid range."
                    )

                else:
                    # Other message types (heartbeats, etc.)
                    logging.debug(f"Skipping message type '{message_type}': {data}")
                    continue

            except Exception as e:
                # If we can't parse the message at all, skip it
                logging.debug(f"Skipping unparseable message: {data} - Error: {e}")
                continue

    async def get_historical_ohlcv(
        self, exchange_symbol: str, interval: str = "1", bars_count: int = 10
    ) -> list[OHLCVBar]:
        """
        Returns a list of historical OHLCV data for a specified symbol.

        This method fetches historical OHLCV data from TradingView and returns it as a list of OHLCVBar objects.
        Symbols are automatically converted from EXCHANGE-SYMBOL to EXCHANGE:SYMBOL format.

        Args:
            exchange_symbol: The symbol in 'EXCHANGE:SYMBOL' or 'EXCHANGE-SYMBOL' format (e.g., 'BINANCE:BTCUSDT' or 'USI-PCC').
            interval: The interval for the chart (default is "1" for 1 minute).
            bars_count: The number of bars to fetch (default is 10).

        Returns:
            A list of OHLCVBar objects containing historical OHLCV data.

        Raises:
            ValueError: If the symbol format is invalid
            WebSocketException: If connection or streaming fails
        """
        await validate_symbols(exchange_symbol)
        # Convert symbol format from EXCHANGE-SYMBOL to EXCHANGE:SYMBOL if needed
        symbol_result = convert_symbol_format(exchange_symbol)
        converted_symbol: str = symbol_result.converted_symbol  # type: ignore
        validate_interval(interval)
        await self._setup_services()

        if not self.connection_service or not self.message_service:
            raise RuntimeError("Services not properly initialized")

        quote_session: str = self.message_service.generate_session(prefix="qs_")
        chart_session: str = self.message_service.generate_session(prefix="cs_")
        logging.info(
            f"Quote session generated: {quote_session}, Chart session generated: {chart_session}"
        )

        send_message_func = self.message_service.get_send_message_callable()
        await self.connection_service.initialize_sessions(
            quote_session, chart_session, send_message_func
        )
        await self.connection_service.add_symbol_to_sessions(
            quote_session,
            chart_session,
            converted_symbol,
            interval,
            bars_count,
            send_message_func,
        )

        historical_bars: list[OHLCVBar] = []
        timeout_seconds: int = 30
        start_time: float = asyncio.get_event_loop().time()

        async for data in self.connection_service.get_data_stream():
            # Check for timeout
            if asyncio.get_event_loop().time() - start_time > timeout_seconds:
                logging.warning(
                    f"Historical data fetch timed out after {timeout_seconds} seconds"
                )
                break

            try:
                # Parse as generic WebSocket message first to check type
                message: WebSocketMessage = WebSocketMessage.model_validate(data)
                message_type: str = message.message_type

                logging.debug(f"Received message type: {message_type}")

                if message_type == "timescale_update":
                    # Parse as timescale update (historical OHLCV data)
                    try:
                        logging.debug(f"Raw timescale_update data: {data}")
                        timescale_response: TimescaleUpdateResponse = (
                            TimescaleUpdateResponse.model_validate(data)
                        )
                        logging.info(
                            f"Received {len(timescale_response.ohlcv_bars)} historical OHLCV bars"
                        )

                        # Log the bars for debugging
                        for bar in timescale_response.ohlcv_bars:
                            logging.debug(f"Parsed OHLCV bar: {bar}")

                        historical_bars.extend(timescale_response.ohlcv_bars)

                        # If we have enough bars or this appears to be the complete dataset, break
                        if len(historical_bars) >= bars_count:
                            break
                    except Exception as e:
                        logging.warning(
                            f"Failed to parse 'timescale_update' message: {e}"
                        )
                        logging.debug(f"Raw message that failed to parse: {data}")
                        continue

                elif message_type == "du":
                    # Parse as OHLCV data update (might contain historical data)
                    try:
                        ohlcv_response: OHLCVResponse = OHLCVResponse.model_validate(
                            data
                        )
                        if ohlcv_response.ohlcv_bars:
                            logging.info(
                                f"Received {len(ohlcv_response.ohlcv_bars)} OHLCV bars from data update"
                            )
                            historical_bars.extend(ohlcv_response.ohlcv_bars)
                    except Exception as e:
                        logging.debug(f"Failed to parse 'du' message as OHLCV: {e}")
                        continue

                elif message_type == "quote_completed":
                    # Quote setup completed - continue waiting for data
                    try:
                        quote_completed: QuoteCompletedMessage = (
                            QuoteCompletedMessage.model_validate(data)
                        )
                        logging.info(
                            f"Quote setup completed for symbol: {quote_completed.symbol}"
                        )
                    except Exception as e:
                        logging.debug(f"Failed to parse 'quote_completed' message: {e}")
                    continue

                elif message_type == "series_loading":
                    # Series loading message - continue waiting for data
                    logging.debug("Series loading for historical data fetch")
                    continue

                elif message_type == "study_loading":
                    # Study loading message - continue waiting for data
                    logging.debug("Study loading for historical data fetch")
                    continue

                elif message_type == "series_completed":
                    # Series completed message - continue waiting for data
                    logging.debug("Series completed for historical data fetch")
                    continue

                elif message_type == "study_completed":
                    # Study completed message - continue waiting for data
                    logging.debug("Study completed for historical data fetch")
                    continue

                elif message_type == "series_error":
                    # Series error - invalid interval or bars count
                    logging.error(
                        "Series error received from TradingView during historical data fetch"
                    )
                    logging.error(f"Error details: {data}")
                    logging.error(
                        "Please check the interval - this timeframe may not be supported for the symbol"
                    )
                    logging.error("Also verify that bars_count is within valid range")

                    # Close connection and raise error
                    if self.connection_service:
                        await self.connection_service.close()

                    raise ValueError(
                        "TradingView series error: Invalid interval or bars count. "
                        "Please check that the timeframe is supported for this symbol "
                        "and that bars_count is within valid range."
                    )

                else:
                    # Other message types - continue waiting
                    logging.debug(
                        f"Skipping message type '{message_type}' in historical data fetch"
                    )
                    continue

            except Exception as e:
                logging.debug(
                    f"Skipping unparseable message in historical fetch: {data} - Error: {e}"
                )
                continue

        # Sort bars by timestamp (chronological order)
        historical_bars.sort(key=lambda bar: bar.timestamp)

        if not historical_bars:
            raise RuntimeError(
                f"No historical data received for symbol {converted_symbol}"
            )

        logging.info(
            f"Successfully fetched {len(historical_bars)} historical OHLCV bars for {converted_symbol}"
        )
        return historical_bars

    async def get_quote_data(
        self, exchange_symbol: str, interval: str = "1", bars_count: int = 10
    ) -> AsyncGenerator[QuoteSymbolData, None]:
        """
        Returns an async generator that yields quote data for a specified symbol in real-time.

        This method is useful for symbols that provide quote data (current price, volume, etc.)
        but may not have OHLCV chart data available. It's ideal for getting real-time price updates.
        Symbols are automatically converted from EXCHANGE-SYMBOL to EXCHANGE:SYMBOL format.

        Args:
            exchange_symbol: The symbol in 'EXCHANGE:SYMBOL' or 'EXCHANGE-SYMBOL' format (e.g., 'NASDAQ:AAPL' or 'USI-PCC').
            interval: The interval for the chart (default is "1" for 1 minute).
            bars_count: The number of bars to fetch (default is 10).

        Returns:
            An async generator yielding quote data as QuoteSymbolData objects.

        Raises:
            ValueError: If the symbol format is invalid
            WebSocketException: If connection or streaming fails

        Example:
            >>> async with OHLCV() as client:
            ...     async for quote in client.get_quote_data("NASDAQ:AAPL", interval="5"):
            ...         print(f"Price: ${quote.current_price}")
        """
        await validate_symbols(exchange_symbol)
        # Convert symbol format from EXCHANGE-SYMBOL to EXCHANGE:SYMBOL if needed
        symbol_result = convert_symbol_format(exchange_symbol)
        converted_symbol: str = symbol_result.converted_symbol  # type: ignore
        validate_interval(interval)
        await self._setup_services()

        if not self.connection_service or not self.message_service:
            raise RuntimeError("Services not properly initialized")

        quote_session: str = self.message_service.generate_session(prefix="qs_")
        chart_session: str = self.message_service.generate_session(prefix="cs_")
        logging.info(
            f"Quote session generated: {quote_session}, Chart session generated: {chart_session}"
        )

        send_message_func = self.message_service.get_send_message_callable()
        await self.connection_service.initialize_sessions(
            quote_session, chart_session, send_message_func
        )
        await self.connection_service.add_symbol_to_sessions(
            quote_session,
            chart_session,
            converted_symbol,
            interval,
            bars_count,
            send_message_func,
        )

        async for data in self.connection_service.get_data_stream():
            try:
                # Parse as generic WebSocket message first to check type
                message: WebSocketMessage = WebSocketMessage.model_validate(data)
                message_type: str = message.message_type

                if message_type == "qsd":
                    # Quote symbol data - contains current price info
                    try:
                        quote_data: QuoteSymbolData = QuoteSymbolData.model_validate(
                            data
                        )
                        yield quote_data
                    except Exception as e:
                        logging.debug(f"Failed to parse 'qsd' message: {e}")
                        continue

                elif message_type == "quote_completed":
                    # Quote setup completed - log but don't yield
                    try:
                        quote_completed: QuoteCompletedMessage = (
                            QuoteCompletedMessage.model_validate(data)
                        )
                        logging.info(
                            f"Quote setup completed for symbol: {quote_completed.symbol}"
                        )
                    except Exception as e:
                        logging.debug(f"Failed to parse 'quote_completed' message: {e}")
                    continue

                elif message_type == "series_loading":
                    # Series loading message - continue waiting for data
                    logging.debug("Series loading for quote data stream")
                    continue

                elif message_type == "study_loading":
                    # Study loading message - continue waiting for data
                    logging.debug("Study loading for quote data stream")
                    continue

                elif message_type == "series_completed":
                    # Series completed message - continue waiting for data
                    logging.debug("Series completed for quote data stream")
                    continue

                elif message_type == "study_completed":
                    # Study completed message - continue waiting for data
                    logging.debug("Study completed for quote data stream")
                    continue

                elif message_type == "series_error":
                    # Series error - invalid interval or bars count
                    logging.error(
                        "Series error received from TradingView during quote data stream"
                    )
                    logging.error(f"Error details: {data}")
                    logging.error(
                        "Please check the interval - this timeframe may not be supported for the symbol"
                    )
                    logging.error("Also verify that bars_count is within valid range")

                    # Close connection and raise error
                    if self.connection_service:
                        await self.connection_service.close()

                    raise ValueError(
                        "TradingView series error: Invalid interval or bars count. "
                        "Please check that the timeframe is supported for this symbol "
                        "and that bars_count is within valid range."
                    )

                else:
                    # Other message types - skip
                    logging.debug(
                        f"Skipping message type '{message_type}' in quote stream"
                    )
                    continue

            except Exception as e:
                # If we can't parse the message at all, skip it
                logging.debug(
                    f"Skipping unparseable message in quote stream: {data} - Error: {e}"
                )
                continue

    async def get_ohlcv_raw(
        self, exchange_symbol: str, interval: str = "1", bars_count: int = 10
    ) -> AsyncGenerator[dict[str, Any], None]:
        """
        Returns an async generator that yields raw OHLC data for a specified symbol in real-time.

        This method provides the raw JSON data from TradingView for debugging purposes.
        Use this when you need to inspect the raw message format or implement custom parsing.
        Symbols are automatically converted from EXCHANGE-SYMBOL to EXCHANGE:SYMBOL format.

        Args:
            exchange_symbol: The symbol in 'EXCHANGE:SYMBOL' or 'EXCHANGE-SYMBOL' format.
            interval: The interval for the chart (default is "1" for 1 minute).
            bars_count: The number of bars to fetch (default is 10).

        Returns:
            An async generator yielding raw OHLC data as JSON dictionary objects.

        Raises:
            ValueError: If the symbol format is invalid
            WebSocketException: If connection or streaming fails

        Example:
            >>> async with OHLCV() as client:
            ...     async for raw_data in client.get_ohlcv_raw("BINANCE:BTCUSDT", interval="5"):
            ...         print(f"Raw message: {raw_data}")
        """
        await validate_symbols(exchange_symbol)
        # Convert symbol format from EXCHANGE-SYMBOL to EXCHANGE:SYMBOL if needed
        symbol_result = convert_symbol_format(exchange_symbol)
        converted_symbol: str = symbol_result.converted_symbol  # type: ignore
        validate_interval(interval)
        await self._setup_services()

        if not self.connection_service or not self.message_service:
            raise RuntimeError("Services not properly initialized")

        quote_session: str = self.message_service.generate_session(prefix="qs_")
        chart_session: str = self.message_service.generate_session(prefix="cs_")
        logging.info(
            f"Quote session generated: {quote_session}, Chart session generated: {chart_session}"
        )

        send_message_func = self.message_service.get_send_message_callable()
        await self.connection_service.initialize_sessions(
            quote_session, chart_session, send_message_func
        )
        await self.connection_service.add_symbol_to_sessions(
            quote_session,
            chart_session,
            converted_symbol,
            interval,
            bars_count,
            send_message_func,
        )

        async for data in self.connection_service.get_data_stream():
            yield data

    async def get_latest_trade_info(
        self, exchange_symbol: List[str]
    ) -> AsyncGenerator[dict[str, Any], None]:
        """
        Returns summary information about multiple symbols including last changes,
        change percentage, and last trade time.

        This method allows you to monitor multiple symbols simultaneously and get
        comprehensive trading information for each. All symbols are automatically
        converted from EXCHANGE-SYMBOL to EXCHANGE:SYMBOL format.

        Args:
            exchange_symbol: A list of symbols in 'EXCHANGE:SYMBOL' or 'EXCHANGE-SYMBOL' format.

        Returns:
            An async generator yielding summary information as JSON dictionary objects.

        Raises:
            ValueError: If any symbol format is invalid
            WebSocketException: If connection or streaming fails

        Example:
            >>> symbols = ["BINANCE:BTCUSDT", "NASDAQ:AAPL", "FOREX:EURUSD"]
            >>> async with OHLCV() as client:
            ...     async for trade_info in client.get_latest_trade_info(symbols):
            ...         print(f"Trade info: {trade_info}")
        """
        await validate_symbols(exchange_symbol)
        # Convert symbol formats from EXCHANGE-SYMBOL to EXCHANGE:SYMBOL if needed
        symbol_results = convert_symbol_format(exchange_symbol)
        # Since exchange_symbol is List[str], symbol_results is List[SymbolConversionResult]
        converted_symbols = [result.converted_symbol for result in symbol_results]  # type: ignore
        await self._setup_services()

        if not self.connection_service or not self.message_service:
            raise RuntimeError("Services not properly initialized")

        quote_session: str = self.message_service.generate_session(prefix="qs_")
        chart_session: str = self.message_service.generate_session(prefix="cs_")
        logging.info(
            f"Session generated: {quote_session}, Chart session generated: {chart_session}"
        )

        send_message_func = self.message_service.get_send_message_callable()
        await self.connection_service.initialize_sessions(
            quote_session, chart_session, send_message_func
        )
        await self.connection_service.add_multiple_symbols_to_sessions(
            quote_session, converted_symbols, send_message_func
        )

        async for data in self.connection_service.get_data_stream():
            yield data


# Signal handler for keyboard interrupt
def signal_handler(sig: int, frame: Optional[types.FrameType]) -> None:
    """
    Handles keyboard interrupt signals to gracefully close the WebSocket connection.

    Args:
        sig: The signal number.
        frame: The current stack frame.
    """
    logging.info("Keyboard interrupt received. Exiting...")
    exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)
