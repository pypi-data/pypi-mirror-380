"""Tests for data module"""

import pytest
import pandas as pd

from riskoptimix import get_data
from riskoptimix.exceptions import ValidationError


def test_get_data_basic():
    """Test basic data fetching"""
    df = get_data("AAPL", start="2024-01-01", end="2024-01-31")

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert all(col in df.columns for col in ["open", "high", "low", "close", "volume"])


def test_get_data_invalid_symbol():
    """Test invalid symbol"""
    with pytest.raises(ValidationError):
        get_data("", start="2024-01-01", end="2024-01-31")

    with pytest.raises(ValidationError):
        get_data(None)


def test_get_data_invalid_dates():
    """Test invalid dates"""
    with pytest.raises(ValidationError):
        get_data("AAPL", start="2024-01-31", end="2024-01-01")


if __name__ == "__main__":
    pytest.main()
