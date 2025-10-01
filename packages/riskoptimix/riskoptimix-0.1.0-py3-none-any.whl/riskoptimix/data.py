"""Data fetching and handling utilities"""

# Import used libraries
import logging
from datetime import datetime, timedelta
from typing import Optional, Union

import pandas as pd
import yfinance as yf

from .exceptions import DataError, ValidationError

logger = logging.getLogger(__name__)


def get_data(
    symbol: str,
    start: Optional[Union[str, datetime]] = None,
    end: Optional[Union[str, datetime]] = None,
    interval: str = "1d",
) -> pd.DataFrame:
    """
    Fetch historical price data for a given symbol.

    Parameters
    ----------
    symbol: str
        Ticker symbol (e.g. 'AAPL', 'BTC-USD')
    start: str or datetime, optional
        Start date for historical data. Defaults to 1 year ago.
    end: str or datetime, optional
        End date for historical data. Defaults to today.
    interval: str, default '1d'
        Data interval: '1m', '5m', '15m', '30m', '1h', '1d', '1wk', '1mo'

    Returns
    -------
    pd.DataFrame
        DataFrame with columns: Open, High, Low, Close, Volume
        Index is DatetimeIndex

    Raises
    ------
    DataError
        If data cannot be fetched or is invalid
    ValidationError
        If input parameters are invalid

    Examples
    --------
    >>> import riskoptimix as ro
    >>> df = ro.get_data('AAPL')
    >>> df = ro.get_data('BTC-USD', start='2024-01-01', end='2024-12-31', interval='1d')
    """

    # Validate inputs
    if not symbol or not isinstance(symbol, str):
        raise ValidationError("Symbol must be a non-empty string")

    # Set default start and end dates
    if end is None:
        end = datetime.now()
    if start is None:
        start = end - timedelta(days=365)

    # Convert string dates to datetime if needed
    if isinstance(start, str):
        start = pd.to_datetime(start)
    if isinstance(end, str):
        end = pd.to_datetime(end)

    # Validate date range
    if start >= end:
        raise ValidationError("Start date must be before end date")

    try:
        # Fetch data from yfinance
        ticker = yf.Ticker(symbol)
        df = ticker.history(
            start=start,
            end=end,
            interval=interval,
        )

        if df.empty:
            raise DataError(f"No data found for {symbol} between {start} and {end}")

        # Clean up the dataframe
        df.index.name = "date"

        # Standardize column names to lowercase
        df.columns = [col.lower() for col in df.columns]

        # Remove any rows with NaN values
        critical_columns = ["open", "high", "low", "close"]
        df = df.dropna(subset=[col for col in critical_columns if col in df.columns])

        logger.info(
            f"Successfully fetched {len(df)} rows of data for {symbol} between {start} and {end}"
        )

        return df

    except Exception as e:
        raise DataError(f"Error fetching data for {symbol}: {e}")
