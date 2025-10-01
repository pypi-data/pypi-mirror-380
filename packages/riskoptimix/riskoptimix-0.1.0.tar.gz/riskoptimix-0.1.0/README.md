# RiskOptimix

A Python toolkit for algorithmic trading focused on data management and technical analysis. RiskOptimix provides utilities for downloading financial data and calculating technical indicators, designed to help algorithmic traders and financial enthusiasts with their analysis workflows.

## Features

### Data Management
- **Historical Data Fetching**: Download price data for stocks, cryptocurrencies, and other financial instruments using Yahoo Finance
- **Data Validation**: Built-in validation and error handling for data integrity
- **Flexible Time Ranges**: Support for various intervals (1m, 5m, 15m, 30m, 1h, 1d, 1wk, 1mo)

### Technical Indicators
- **Moving Averages**: Simple Moving Average (SMA), Exponential Moving Average (EMA), Weighted Moving Average (WMA)
- **Momentum Indicators**: RSI, Stochastic Oscillator, Williams %R, Rate of Change (ROC)
- **Volatility Indicators**: Bollinger Bands, Average True Range (ATR), Standard Deviation
- **Volume Indicators**: Volume Weighted Average Price (VWAP), On-Balance Volume (OBV)
- **Trend Indicators**: MACD, Parabolic SAR, Average Directional Index (ADX)
- **Support/Resistance**: Pivot Points, Fibonacci Retracements
- **Batch Processing**: Apply multiple indicators at once using predefined profiles

## Installation

```bash
pip install riskoptimix
```

## Quick Start

### Basic Data Fetching

```python
import riskoptimix as ro

# Fetch one year of daily data for Apple
df = ro.get_data('AAPL')

# Fetch specific date range with hourly data
df = ro.get_data('BTC-USD', start='2024-01-01', end='2024-12-31', interval='1h')
```

### Technical Indicators

```python
from riskoptimix.indicators import sma, ema, rsi, bollinger_bands

# Calculate individual indicators
df['SMA_20'] = sma(df['close'], period=20)
df['EMA_20'] = ema(df['close'], period=20)
df['RSI_14'] = rsi(df['close'], period=14)

# Calculate Bollinger Bands
bb_upper, bb_middle, bb_lower = bollinger_bands(df['close'], period=20, std_dev=2)
df['BB_Upper'] = bb_upper
df['BB_Middle'] = bb_middle
df['BB_Lower'] = bb_lower
```

### Batch Indicator Processing

```python
from riskoptimix.indicators import prepare_data

# Apply basic indicators (SMA, EMA, RSI)
df_basic = prepare_data(df, profile='basic')

# Apply momentum-focused indicators
df_momentum = prepare_data(df, profile='momentum')

# Apply custom set of indicators
df_custom = prepare_data(
    df, 
    profile='custom',
    custom_indicators=['sma_10', 'sma_30', 'rsi_21', 'bb', 'vwap']
)

# Apply all available indicators
df_full = prepare_data(df, profile='all')
```

## Examples

Check the `examples/` directory for detailed usage examples:
- `basic_example.py`: Simple data fetching and indicator calculation
- `indicators_example.py`: Various indicator profiles and batch processing

## Requirements

- Python >=3.8
- pandas >=1.5.0
- numpy >=1.20.0
- yfinance >=0.2.0
- requests >=2.28.0

## Development Status

RiskOptimix is currently in **alpha** stage (v0.1.0). The package includes:

**Current Features:**
- Data fetching from Yahoo Finance
- 25+ technical indicators
- Batch indicator processing
- Error handling and validation

**Planned Features:**
- Backtesting framework
- Risk management tools
- Portfolio optimization
- Plotting and visualization utilities
- Additional data sources
- Strategy templates
- Performance metrics

## Contributing

This is an early-stage project. Contributions, suggestions, and feedback are welcome. Please feel free to open issues or submit pull requests.

## License

MIT License - see LICENSE file for details.

## Disclaimer

This software is for educational and research purposes only. It is not intended as financial advice. Trading financial instruments involves substantial risk of loss. Past performance does not guarantee future results.
