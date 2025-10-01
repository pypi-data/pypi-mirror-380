"""Tests for indicators module"""

# Import used libraries
import pytest
import pandas as pd
import numpy as np
import warnings

from riskoptimix.indicators import (
    sma,
    ema,
    rsi,
    macd,
    stochastic,
    rate_of_change,
    bollinger_bands,
    atr,
    volatility,
    obv,
    vwap,
    volume_ratio,
    adx,
    prepare_data,
)
from riskoptimix.exceptions import ValidationError


@pytest.fixture
def sample_data():
    """Create sample OHLCV data for testing"""
    np.random.seed(42)
    dates = pd.date_range("2023-01-01", periods=100, freq="D")

    # Generate realistic price data
    base_price = 100
    returns = np.random.normal(0.001, 0.02, 100)
    prices = [base_price]

    for ret in returns:
        prices.append(prices[-1] * (1 + ret))

    df = pd.DataFrame(
        {
            "open": prices[:-1],
            "high": [p * (1 + abs(np.random.normal(0, 0.01))) for p in prices[:-1]],
            "low": [p * (1 - abs(np.random.normal(0, 0.01))) for p in prices[:-1]],
            "close": prices[1:],
            "volume": np.random.randint(1000, 10000, 100),
        },
        index=dates,
    )

    return df


@pytest.fixture
def simple_prices():
    """Simple price series for basic testing"""
    return pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# ========================================================
# Basic Indicators Tests
# ========================================================


def test_sma(simple_prices):
    """Test SMA function"""
    result = sma(simple_prices, period=3)

    assert len(result) == len(simple_prices)
    assert result.iloc[2] == 2.0  # (1+2+3)/3
    assert result.iloc[-1] == 9.0  # (8+9+10)/3


def test_sma_invalid_period(simple_prices):
    """Test SMA function with invalid period"""
    with pytest.raises(ValidationError):
        sma(simple_prices, period=0)


def test_ema(simple_prices):
    """Test EMA function"""
    result = ema(simple_prices, period=3)

    assert len(result) == len(simple_prices)
    assert not result.iloc[:2].isna().any()  # Should have values from start


def test_ema_invalid_period(simple_prices):
    """Test EMA function with invalid period"""
    with pytest.raises(ValidationError):
        ema(simple_prices, period=-1)


# ========================================================
# Momentum Indicators Tests
# ========================================================


def test_rsi(sample_data):
    """Test RSI calculation"""
    result = rsi(sample_data["close"], period=14)

    assert len(result) == len(sample_data)
    # RSI should be between 0 and 100 (excluding NaN values)
    valid_values = result.dropna()
    assert (valid_values >= 0).all() and (valid_values <= 100).all()


def test_rsi_invalid_period(simple_prices):
    """Test RSI with invalid period"""
    with pytest.raises(ValidationError):
        rsi(simple_prices, period=0)


def test_macd(sample_data):
    """Test MACD calculation"""
    result = macd(sample_data["close"])

    assert isinstance(result, pd.DataFrame)
    assert all(col in result.columns for col in ["macd", "signal", "histogram"])
    assert len(result) == len(sample_data)


def test_macd_invalid_periods(simple_prices):
    """Test MACD with invalid periods"""
    with pytest.raises(ValidationError):
        macd(simple_prices, fast_period=0)


def test_stochastic(sample_data):
    """Test Stochastic Oscillator"""
    result = stochastic(sample_data["high"], sample_data["low"], sample_data["close"])

    assert isinstance(result, pd.DataFrame)
    assert all(col in result.columns for col in ["k", "d"])
    assert len(result) == len(sample_data)


def test_rate_of_change(simple_prices):
    """Test Rate of Change"""
    result = rate_of_change(simple_prices, period=2)

    assert len(result) == len(simple_prices)
    # ROC at index 2 should be (3-1)/1 * 100 = 200%
    assert abs(result.iloc[2] - 200.0) < 0.01


# ========================================================
# Volatility Indicators Tests
# ========================================================


def test_bollinger_bands(sample_data):
    """Test Bollinger Bands"""
    result = bollinger_bands(sample_data["close"])

    assert isinstance(result, pd.DataFrame)
    assert all(col in result.columns for col in ["middle", "upper", "lower"])
    assert len(result) == len(sample_data)

    # Upper band should be above middle, lower band should be below
    valid_data = result.dropna()
    assert (valid_data["upper"] >= valid_data["middle"]).all()
    assert (valid_data["lower"] <= valid_data["middle"]).all()


def test_atr(sample_data):
    """Test Average True Range"""
    result = atr(sample_data["high"], sample_data["low"], sample_data["close"])

    assert len(result) == len(sample_data)
    # ATR should be positive
    valid_values = result.dropna()
    assert (valid_values >= 0).all()


def test_atr_invalid_period(sample_data):
    """Test ATR with invalid period"""
    with pytest.raises(ValidationError):
        atr(sample_data["high"], sample_data["low"], sample_data["close"], period=0)


def test_volatility(sample_data):
    """Test volatility calculation"""
    result = volatility(sample_data["close"], period=20)

    assert len(result) == len(sample_data)
    # Volatility should be positive
    valid_values = result.dropna()
    assert (valid_values >= 0).all()


def test_volatility_annualized(sample_data):
    """Test annualized volatility"""
    result_normal = volatility(sample_data["close"], period=20, annualized=False)
    result_annual = volatility(sample_data["close"], period=20, annualized=True)

    # Annualized should be higher than normal (multiplied by sqrt(252))
    valid_normal = result_normal.dropna()
    valid_annual = result_annual.dropna()

    if len(valid_normal) > 0 and len(valid_annual) > 0:
        assert valid_annual.iloc[-1] > valid_normal.iloc[-1]


# ========================================================
# Volume Indicators Tests
# ========================================================


def test_obv(sample_data):
    """Test On Balance Volume"""
    result = obv(sample_data["close"], sample_data["volume"])

    assert len(result) == len(sample_data)
    assert result.iloc[0] == 0  # OBV starts at 0


def test_obv_invalid_length():
    """Test OBV with mismatched series lengths"""
    prices = pd.Series([1, 2, 3])
    volume = pd.Series([100, 200])  # Different length

    with pytest.raises(ValidationError):
        obv(prices, volume)


def test_vwap(sample_data):
    """Test Volume Weighted Average Price"""
    result = vwap(
        sample_data["high"],
        sample_data["low"],
        sample_data["close"],
        sample_data["volume"],
    )

    assert len(result) == len(sample_data)
    # VWAP should be positive
    assert (result > 0).all()


def test_vwap_invalid_length():
    """Test VWAP with mismatched series lengths"""
    high = pd.Series([1, 2, 3])
    low = pd.Series([0.5, 1.5, 2.5])
    close = pd.Series([0.8, 1.8, 2.8])
    volume = pd.Series([100, 200])  # Different length

    with pytest.raises(ValidationError):
        vwap(high, low, close, volume)


def test_volume_ratio(sample_data):
    """Test Volume Ratio"""
    result = volume_ratio(sample_data["volume"], period=10)

    assert len(result) == len(sample_data)
    # Volume ratio should be positive
    valid_values = result.dropna()
    assert (valid_values > 0).all()


# ========================================================
# Trend Indicators Tests
# ========================================================


def test_adx(sample_data):
    """Test Average Directional Index"""
    result = adx(sample_data["high"], sample_data["low"], sample_data["close"])

    assert len(result) == len(sample_data)
    # ADX should be between 0 and 100
    valid_values = result.dropna()
    assert (valid_values >= 0).all() and (valid_values <= 100).all()


def test_adx_invalid_length():
    """Test ADX with mismatched series lengths"""
    high = pd.Series([1, 2, 3])
    low = pd.Series([0.5, 1.5])  # Different length
    close = pd.Series([0.8, 1.8, 2.8])

    with pytest.raises(ValidationError):
        adx(high, low, close)


# ========================================================
# Data Preparation Tests
# ========================================================


def test_prepare_data_basic_profile(sample_data):
    """Test prepare_data with basic profile"""
    result = prepare_data(sample_data, profile="basic")

    # Should have original columns plus indicators
    expected_indicators = ["sma_20", "sma_50", "rsi_14", "volume_ratio"]
    for indicator in expected_indicators:
        assert indicator in result.columns

    assert len(result) == len(sample_data)


def test_prepare_data_momentum_profile(sample_data):
    """Test prepare_data with momentum profile"""
    result = prepare_data(sample_data, profile="momentum")

    # Check for MACD columns (should be expanded)
    assert "macd_macd" in result.columns
    assert "macd_signal" in result.columns
    assert "macd_histogram" in result.columns

    # Check other momentum indicators
    assert "rsi_14" in result.columns
    assert "roc_10" in result.columns


def test_prepare_data_custom_profile(sample_data):
    """Test prepare_data with custom indicators"""
    custom_indicators = ["sma_20", "rsi_14", "bb"]
    result = prepare_data(
        sample_data, profile="custom", custom_indicators=custom_indicators
    )

    assert "sma_20" in result.columns
    assert "rsi_14" in result.columns
    assert "bb_middle" in result.columns  # Bollinger bands expands


def test_prepare_data_invalid_dataframe():
    """Test prepare_data with invalid input"""
    with pytest.raises(ValidationError):
        prepare_data("not a dataframe")


def test_prepare_data_empty_dataframe():
    """Test prepare_data with empty dataframe"""
    empty_df = pd.DataFrame()
    with pytest.raises(ValidationError):
        prepare_data(empty_df)


def test_prepare_data_missing_columns():
    """Test prepare_data with missing required columns"""
    incomplete_df = pd.DataFrame({"close": [1, 2, 3]})
    with pytest.raises(ValidationError):
        prepare_data(incomplete_df)


def test_prepare_data_invalid_profile(sample_data):
    """Test prepare_data with invalid profile"""
    with pytest.raises(ValidationError):
        prepare_data(sample_data, profile="invalid_profile")


def test_prepare_data_custom_without_indicators(sample_data):
    """Test prepare_data custom profile without custom_indicators"""
    with pytest.raises(ValidationError):
        prepare_data(sample_data, profile="custom")


def test_prepare_data_unknown_custom_indicator(sample_data):
    """Test prepare_data with unknown custom indicator"""
    # Should raise ValidationError when no valid indicators are found
    with pytest.raises(ValidationError, match="No valid indicators found"):
        prepare_data(
            sample_data, profile="custom", custom_indicators=["unknown_indicator"]
        )


def test_prepare_data_mixed_custom_indicators(sample_data):
    """Test prepare_data with mix of valid and invalid custom indicators"""
    # Should issue warning for unknown but still process valid ones
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        result = prepare_data(
            sample_data,
            profile="custom",
            custom_indicators=["sma_20", "unknown_indicator"],
        )
        assert len(w) > 0
        assert "Unknown indicator" in str(w[0].message)
        assert "sma_20" in result.columns


def test_prepare_data_non_numeric_columns():
    """Test prepare_data with non-numeric columns"""
    bad_df = pd.DataFrame(
        {
            "open": [1, 2, 3],
            "high": [1.5, 2.5, 3.5],
            "low": [0.5, 1.5, 2.5],
            "close": ["a", "b", "c"],  # Non-numeric
            "volume": [100, 200, 300],
        }
    )

    with pytest.raises(ValidationError):
        prepare_data(bad_df)


if __name__ == "__main__":
    pytest.main()
