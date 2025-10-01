"""Technical indicators for trading"""

# Import used libraries
import pandas as pd
import numpy as np
import warnings
from typing import Literal, Optional, List

from .exceptions import ValidationError


# ========================================================
# Basic indicators
# ========================================================


def sma(prices: pd.Series, period: int = 20) -> pd.Series:
    """Calculate the Simple Moving Average (SMA)

    Parameters
    ----------
    prices: pd.Series
        The prices to calculate the SMA for
    period: int, default 20
        The number of periods to calculate the SMA for

    Returns
    -------
    pd.Series
        The SMA values

    Raises
    ------
    ValidationError
        If the period is less than 1

    Examples
    --------
    >>> sma_20 = sma(df['close'], period=20)
    """

    if period < 1:
        raise ValidationError("Period must be at least 1")

    return prices.rolling(window=period).mean()


def ema(prices: pd.Series, period: int = 20) -> pd.Series:
    """Calculate the Exponential Moving Average (EMA)

    Parameters
    ----------
    prices: pd.Series
        The prices to calculate the EMA for
    period: int, default 20
        The number of periods to calculate the EMA for


    Returns
    -------
    pd.Series
        The EMA values

    Raises
    ------
    ValidationError
        If the period is less than 1

    Examples
    --------
    >>> ema_20 = ema(df['close'], period=20)
    """

    if period < 1:
        raise ValidationError("Period must be at least 1")

    return prices.ewm(span=period, adjust=False).mean()


# ========================================================
# Momentum indicators
# ========================================================


def rsi(prices: pd.Series, period: int = 14) -> pd.Series:
    """
    Calculate the Relative Strength Index (RSI)

    Parameters
    ----------
    prices: pd.Series
        Series of prices
    period: int, default 14
        The number of periods to calculate the RSI for

    Returns
    -------
    pd.Series
        The RSI values (0-100)

    Raises
    ------
    ValidationError
        If the period is less than 1

    Examples
    --------
    >>> rsi_14 = rsi(df['close'], period=14)
    """

    if period < 1:
        raise ValidationError("Period must be at least 1")

    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


def macd(
    prices: pd.Series,
    fast_period: int = 12,
    slow_period: int = 26,
    signal_period: int = 9,
) -> pd.DataFrame:
    """Calculate the Moving Average Convergence Divergence (MACD)

    Parameters
    ----------
    prices: pd.Series
        Series of prices
    fast_period: int, default 12
        The number of periods for the fast EMA
    slow_period: int, default 26
        The number of periods for the slow EMA
    signal_period: int, default 9
        The number of periods for the signal line

    Returns
    -------
    pd.DataFrame
        DataFrame with columns: macd, signal, histogram

    Raises
    ------
    ValidationError
        If the fast_period, slow_period, or signal_period is less than 1

    Examples
    --------
    >>> macd_12_26_9 = macd(df['close'], fast_period=12, slow_period=26, signal_period=9)
    """

    if fast_period < 1 or slow_period < 1 or signal_period < 1:
        raise ValidationError("All periods must be at least 1")

    ema_fast = ema(prices, period=fast_period)
    ema_slow = ema(prices, period=slow_period)

    macd_line = ema_fast - ema_slow
    signal_line = ema(macd_line, period=signal_period)
    histogram = macd_line - signal_line

    return pd.DataFrame(
        {"macd": macd_line, "signal": signal_line, "histogram": histogram},
        index=prices.index,
    )


def stochastic(
    high: pd.Series,
    low: pd.Series,
    close: pd.Series,
    period: int = 14,
    smooth_k: int = 3,
    smooth_d: int = 3,
) -> pd.DataFrame:
    """Calculate the Stochastic Oscillator

    Parameters
    ----------
    high: pd.Series
        Series of high prices
    low: pd.Series
        Series of low prices
    close: pd.Series
        Series of closing prices
    period: int, default 14
        The number of periods to calculate the Stochastic Oscillator for
    smooth_k: int, default 3
        The number of periods to smooth the %K line
    smooth_d: int, default 3
        The number of periods to smooth the %D line

    Returns
    -------
    pd.DataFrame
        DataFrame with columns: k, d

    Raises
    ------
    ValidationError
        If the period, smooth_k, or smooth_d is less than 1

    Examples
    --------
    >>> stochastic_14_3_3 = stochastic(df['high'], df['low'], df['close'], period=14, smooth_k=3, smooth_d=3)
    """

    if period < 1 or smooth_k < 1 or smooth_d < 1:
        raise ValidationError("All periods must be at least 1")

    lowest_low = low.rolling(window=period).min()
    highest_high = high.rolling(window=period).max()

    # Calculate %K
    k_percent = 100 * ((close - lowest_low) / (highest_high - lowest_low))

    # Smooth %K
    k_smooth = k_percent.rolling(window=smooth_k).mean()

    # Calculate %D (signal line)
    d_percent = k_smooth.rolling(window=smooth_d).mean()

    return pd.DataFrame({"k": k_smooth, "d": d_percent}, index=close.index)


def rate_of_change(prices: pd.Series, period: int = 10) -> pd.Series:
    """
    Calculate the Rate of Change (ROC)

    Parameters
    ----------
    prices: pd.Series
        Series of prices
    period: int, default 10
        The number of periods to calculate the ROC for

    Returns
    -------
    pd.Series
        Rate of Change values (percentage)

    Raises
    ------
    ValidationError
        If the period is less than 1

    Examples
    --------
    >>> roc_10 = rate_of_change(df['close'], period=10)
    """

    if period < 1:
        raise ValidationError("Period must be at least 1")

    return ((prices - prices.shift(period)) / prices.shift(period)) * 100


# ========================================================
# Volatility indicators
# ========================================================


def bollinger_bands(
    prices: pd.Series, period: int = 20, std_dev: int = 2
) -> pd.DataFrame:
    """
    Calculate the Bollinger Bands

    Parameters
    ----------
    prices: pd.Series
        Series of prices
    period: int, default 20
        Period for moving average
    std_dev: int, default 2
        Number of standard deviations for the bands

    Returns
    -------
    pd.DataFrame
        DataFrame with columns: middle, upper, lower

    Raises
    ------
    ValidationError
        If the period is less than 1

    Examples
    --------
    >>> bollinger_bands_20_2 = bollinger_bands(df['close'], period=20, std_dev=2)
    """

    if period < 1:
        raise ValidationError("Period must be at least 1")

    middle_band = sma(prices, period=period)
    std = prices.rolling(window=period).std()

    upper_band = middle_band + (std_dev * std)
    lower_band = middle_band - (std_dev * std)

    return pd.DataFrame(
        {"middle": middle_band, "upper": upper_band, "lower": lower_band},
        index=prices.index,
    )


def atr(
    high: pd.Series, low: pd.Series, close: pd.Series, period: int = 14
) -> pd.Series:
    """
    Calculate the Average True Range (ATR)

    Parameters
    ----------
    high: pd.Series
        Series of high prices
    low: pd.Series
        Series of low prices
    close: pd.Series
        Series of closing prices
    period: int, default 14
        Period for ATR

    Returns
    -------
    pd.Series
        Series with ATR values

    Raises
    ------
    ValidationError
        If the period is less than 1

    Examples
    --------
    >>> atr_14 = atr(df['high'], df['low'], df['close'], period=14)
    """

    if period < 1:
        raise ValidationError("Period must be at least 1")

    high_low = high - low
    high_close = np.abs(high - close.shift(1))
    low_close = np.abs(low - close.shift(1))

    true_range = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)

    return true_range.rolling(window=period).mean()


def volatility(
    prices: pd.Series, period: int = 20, annualized: bool = False
) -> pd.Series:
    """
    Calculate the simple volatility (std of the returns)

    Parameters
    ----------
    prices: pd.Series
        Series of prices
    period: int, default 20
        Period for volatility
    annualized: bool, default False
        Whether to annualize the volatility

    Returns
    -------
    pd.Series
        Series with volatility values

    Raises
    ------
    ValidationError
        If the period is less than 1

    Examples
    --------
    >>> volatility_20 = volatility(df['close'], period=20)
    >>> volatility_20_annualized = volatility(df['close'], period=20, annualized=True)
    """

    if period < 1:
        raise ValidationError("Period must be at least 1")

    returns = prices.pct_change()
    vol = returns.rolling(window=period).std()

    if annualized:
        return vol * np.sqrt(252)

    return vol


# ========================================================
# Volume indicators
# ========================================================


def obv(prices: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Calculate the On Balance Volume (OBV)

    Parameters
    ----------
    prices: pd.Series
        Series of closing prices
    volume: pd.Series
        Series of volume data

    Returns
    -------
    pd.Series
        Series with OBV values

    Raises
    ------
    ValidationError
        If the input series have different lengths

    Examples
    --------
    >>> obv_values = obv(df['close'], df['volume'])
    """

    if len(prices) != len(volume):
        raise ValidationError("Price and volume series must have the same length")

    price_diff = prices.diff()

    obv_values = pd.Series(index=prices.index, dtype=float)
    obv_values.iloc[0] = 0  # OBV typically starts at 0

    for i in range(1, len(prices)):
        if price_diff.iloc[i] > 0:
            obv_values.iloc[i] = obv_values.iloc[i - 1] + volume.iloc[i]
        elif price_diff.iloc[i] < 0:
            obv_values.iloc[i] = obv_values.iloc[i - 1] - volume.iloc[i]
        else:
            obv_values.iloc[i] = obv_values.iloc[i - 1]

    return obv_values


def vwap(
    high: pd.Series,
    low: pd.Series,
    close: pd.Series,
    volume: pd.Series,
) -> pd.Series:
    """
    Calculate the Volume Weighted Average Price (VWAP)

    Parameters
    ----------
    high: pd.Series
        Series of high prices
    low: pd.Series
        Series of low prices
    close: pd.Series
        Series of closing prices
    volume: pd.Series
        Series of volume data

    Returns
    -------
    pd.Series
        Series with VWAP values

    Raises
    ------
    ValidationError
        If the input series have different lengths

    Examples
    --------
    >>> vwap_values = vwap(df['high'], df['low'], df['close'], df['volume'])
    """

    if len(high) != len(low) or len(high) != len(close) or len(high) != len(volume):
        raise ValidationError("All input series must have the same length")

    typical_price = (high + low + close) / 3
    vwap_values = (typical_price * volume).cumsum() / volume.cumsum()

    return vwap_values


def volume_ratio(volume: pd.Series, period: int = 20) -> pd.Series:
    """
    Calculate the Volume Ratio (current volume / average volume)

    Parameters
    ----------
    volume: pd.Series
        Series of volume data
    period: int, default 20
        Period for average volume

    Returns
    -------
    pd.Series
        Series with Volume Ratio values

    Raises
    ------
    ValidationError
        If the period is less than 1

    Examples
    --------
    >>> volume_ratio_20 = volume_ratio(df['volume'], period=20)
    """

    if period < 1:
        raise ValidationError("Period must be at least 1")

    average_volume = volume.rolling(window=period).mean()
    volume_ratio = volume / average_volume

    return volume_ratio


# ========================================================
# Trend indicators
# ========================================================


def adx(
    high: pd.Series, low: pd.Series, close: pd.Series, period: int = 14
) -> pd.Series:
    """
    Calculate the Average Directional Index (ADX)

    Parameters
    ----------
    high: pd.Series
        Series of high prices
    low: pd.Series
        Series of low prices
    close: pd.Series
        Series of closing prices
    period: int, default 14
        Period for calculation

    Returns
    -------
    pd.Series
        Series with ADX values

    Raises
    ------
    ValidationError
        If the period is less than 1 or input series have different lengths

    Examples
    --------
    >>> adx_14 = adx(df['high'], df['low'], df['close'], period=14)
    """

    if period < 1:
        raise ValidationError("Period must be at least 1")

    if len(high) != len(low) or len(high) != len(close):
        raise ValidationError("All input series must have the same length")

    # Calculate True Range (TR)
    high_low = high - low
    high_close = np.abs(high - close.shift(1))
    low_close = np.abs(low - close.shift(1))
    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)

    # Calculate directional movements
    up_move = high.diff()
    down_move = low.diff()

    pos_dm = pd.Series(0.0, index=high.index)
    neg_dm = pd.Series(0.0, index=high.index)

    # +DM when up_move > down_move and up_move > 0
    pos_dm[(up_move > down_move) & (up_move > 0)] = up_move[
        (up_move > down_move) & (up_move > 0)
    ]

    # -DM when down_move > up_move and down_move > 0
    neg_dm[(down_move > up_move) & (down_move > 0)] = down_move[
        (down_move > up_move) & (down_move > 0)
    ]

    # Apply Wilder's smoothing (similar to EMA with alpha = 1/period)
    alpha = 1.0 / period

    tr_smooth = tr.ewm(alpha=alpha, adjust=False).mean()
    pos_dm_smooth = pos_dm.ewm(alpha=alpha, adjust=False).mean()
    neg_dm_smooth = neg_dm.ewm(alpha=alpha, adjust=False).mean()

    # Calculate +DI and -DI
    pos_di = 100 * (pos_dm_smooth / tr_smooth)
    neg_di = 100 * (neg_dm_smooth / tr_smooth)

    # Calculate DX
    dx = 100 * np.abs(pos_di - neg_di) / (pos_di + neg_di)

    # Calculate ADX (smoothed DX)
    adx_values = dx.ewm(alpha=alpha, adjust=False).mean()

    return adx_values


# ========================================================
# Dataset preperation functions
# ========================================================


def prepare_data(
    df: pd.DataFrame,
    profile: Literal[
        "basic", "momentum", "volatility", "volume", "trend", "all", "custom"
    ] = "basic",
    custom_indicators: Optional[List[str]] = None,
    **kwargs,
) -> pd.DataFrame:
    """
    Prepare a dataset by adding multiple technical indicators based on a profile.

    Parameters
    ----------
    df: pd.DataFrame
        The dataset to prepare, must have OHLCV data
    profile: str, default 'basic'
        The profile determining which indicators to add
        - 'basic': Simple indicators (SMA, RSI, Volume Ratio)
        - 'momentum': Momentum-based indicators (RSI, MACD, Stochastic, ROC)
        - 'volatility': Volatility-based indicators (ATR, Bollinger Bands, Volatility)
        - 'volume': Volume-based indicators (OBV, VWAP, Volume Ratio)
        - 'trend': Trend-based indicators (SMA, EMA, ADX, MACD)
        - 'all': All indicators
        - 'custom': Custom indicators, must be provided in custom_indicators
    custom_indicators: list, optional
        List of custom indicators to add, must be a function from the indicators module
    **kwargs: dict
        Additional parameters for specific indicators (e.g. sma_period=50)

    Returns
    -------
    pd.DataFrame
        Original dataframe with additional indicator columns

    Raises
    ------
    ValidationError
        If the input is not a pandas DataFrame, if the dataframe is empty,
        if required columns are missing, if columns contain non-numeric data,
        if the profile is invalid, if custom indicators are not provided for
        custom profile, if no valid indicators are found in custom_indicators,
        or if there's an error calculating any indicator
    UserWarning
        If an unknown indicator is specified in custom_indicators, if an
        indicator returns None or empty results, or if an indicator returns
        an unexpected data type

    Examples
    --------
    >>> df = ro.get_data('AAPL')
    >>> df = prepare_data(df, profile='momentum')
    >>> df = prepare_data(df, profile='custom', custom_indicators=['sma_20', 'rsi_14'])
    """

    # Validate input dataframe
    if not isinstance(df, pd.DataFrame):
        raise ValidationError("Input must be a pandas DataFrame")

    if df.empty:
        raise ValidationError("Input dataframe cannot be empty")

    # Create a copy of the dataframe
    result = df.copy()

    # Validate required columns
    required_cols = ["open", "high", "low", "close", "volume"]
    missing_cols = [col for col in required_cols if col not in result.columns]
    if missing_cols:
        raise ValidationError(f"Missing required columns: {missing_cols}")

    # Validate that required columns contain numeric data
    for col in required_cols:
        if not pd.api.types.is_numeric_dtype(result[col]):
            raise ValidationError(f"Column '{col}' must contain numeric data")

    # Define indicator profiles
    profiles = {
        "basic": {
            "sma_20": lambda: sma(result["close"], period=20),
            "sma_50": lambda: sma(result["close"], period=50),
            "rsi_14": lambda: rsi(result["close"], period=14),
            "volume_ratio": lambda: volume_ratio(result["volume"], period=20),
        },
        "momentum": {
            "rsi_14": lambda: rsi(result["close"], period=14),
            "rsi_9": lambda: rsi(result["close"], period=9),
            "macd": lambda: macd(result["close"]),
            "stochastic": lambda: stochastic(
                result["high"], result["low"], result["close"]
            ),
            "roc_10": lambda: rate_of_change(result["close"], period=10),
        },
        "volatility": {
            "bb": lambda: bollinger_bands(result["close"]),
            "atr_14": lambda: atr(
                result["high"], result["low"], result["close"], period=14
            ),
            "volatility_20": lambda: volatility(result["close"], period=20),
        },
        "volume": {
            "obv": lambda: obv(result["close"], result["volume"]),
            "vwap": lambda: vwap(
                result["high"], result["low"], result["close"], result["volume"]
            ),
            "volume_ratio": lambda: volume_ratio(result["volume"], period=20),
            "volume_sma": lambda: sma(result["volume"], period=20),
        },
        "trend": {
            "sma_10": lambda: sma(result["close"], period=10),
            "sma_20": lambda: sma(result["close"], period=20),
            "sma_50": lambda: sma(result["close"], period=50),
            "ema_12": lambda: ema(result["close"], period=12),
            "ema_26": lambda: ema(result["close"], period=26),
            "macd": lambda: macd(result["close"]),
            "adx_14": lambda: adx(
                result["high"], result["low"], result["close"], period=14
            ),
        },
        "all": {},
    }

    # Build all profile
    for profile_indicators in profiles.values():
        if profile_indicators:  # Skip all itself
            profiles["all"].update(profile_indicators)

    # Additional indicators for all
    profiles["all"].update(
        {
            "sma_200": lambda: sma(result["close"], period=200),
            "ema_50": lambda: ema(result["close"], period=50),
            "rsi_21": lambda: rsi(result["close"], period=21),
            "atr_20": lambda: atr(
                result["high"], result["low"], result["close"], period=20
            ),
        }
    )

    # Handle custom profile
    if profile == "custom":
        if not custom_indicators:
            raise ValidationError(
                "Custom profile requires custom_indicators (e.g. ['sma_20', 'rsi_14'])"
            )

        indicators_to_add = {}
        for indicator_spec in custom_indicators:
            # Parse the indicator name (e.g. 'sma_20' -> ('sma', 20))
            parts = indicator_spec.split("_")
            indicator_name = parts[0]

            # Try to parse period if involved
            period = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else None

            # Map to functions
            if indicator_name == "sma" and period:
                indicators_to_add[indicator_spec] = lambda p=period: sma(
                    result["close"], p
                )
            elif indicator_name == "ema" and period:
                indicators_to_add[indicator_spec] = lambda p=period: ema(
                    result["close"], p
                )
            elif indicator_name == "rsi" and period:
                indicators_to_add[indicator_spec] = lambda p=period: rsi(
                    result["close"], p
                )
            elif indicator_name == "atr" and period:
                indicators_to_add[indicator_spec] = lambda p=period: atr(
                    result["high"], result["low"], result["close"], p
                )
            elif indicator_name == "bb":
                indicators_to_add["bb"] = lambda: bollinger_bands(result["close"])
            elif indicator_name == "macd":
                indicators_to_add["macd"] = lambda: macd(result["close"])
            elif indicator_name == "obv":
                indicators_to_add["obv"] = lambda: obv(
                    result["close"], result["volume"]
                )
            elif indicator_name == "vwap":
                indicators_to_add["vwap"] = lambda: vwap(
                    result["high"], result["low"], result["close"], result["volume"]
                )
            else:
                warnings.warn(f"Unknown indicator: {indicator_spec}")
                continue  # Skip unknown indicators instead of adding them

        # Only proceed if we have indicators to add
        if not indicators_to_add:
            raise ValidationError("No valid indicators found in custom_indicators")
    else:
        # Use predefined profile
        if profile not in profiles:
            raise ValidationError(
                f"Invalid profile: {profile}. Choose from {list(profiles.keys())}"
            )

        indicators_to_add = profiles[profile]

    # Add indicators to the dataframe
    for indicator_name, indicator_func in indicators_to_add.items():
        try:
            indicator_result = indicator_func()

            # Validate indicator result
            if indicator_result is None:
                warnings.warn(f"Indicator {indicator_name} returned None, skipping")
                continue

            # Handle different return types
            if isinstance(indicator_result, pd.DataFrame):
                # For indicators that have multiple columns, add each column as a separate column
                if indicator_result.empty:
                    warnings.warn(
                        f"Indicator {indicator_name} returned empty DataFrame, skipping"
                    )
                    continue
                for col in indicator_result.columns:
                    result[f"{indicator_name}_{col}"] = indicator_result[col]
            elif isinstance(indicator_result, pd.Series):
                # For single-column indicators, add as is
                if indicator_result.empty:
                    warnings.warn(
                        f"Indicator {indicator_name} returned empty Series, skipping"
                    )
                    continue
                result[indicator_name] = indicator_result
            else:
                warnings.warn(
                    f"Indicator {indicator_name} returned unexpected type {type(indicator_result)}, skipping"
                )
                continue

        except Exception as e:
            raise ValidationError(
                f"Error calculating indicator '{indicator_name}': {str(e)}"
            )

    return result
