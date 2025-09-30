# CryptoHFTData Python SDK

[![PyPI version](https://badge.fury.io/py/cryptohftdata.svg)](https://badge.fury.io/py/cryptohftdata)
[![Python versions](https://img.shields.io/pypi/pyversions/cryptohftdata.svg)](https://pypi.org/project/cryptohftdata/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation Status](https://readthedocs.org/projects/cryptohftdata/badge/?version=latest)](https://cryptohftdata.readthedocs.io/en/latest/?badge=latest)

A Python SDK for accessing cryptocurrency high-frequency trading data with a simple and intuitive API.

## Installation

```bash
pip install cryptohftdata
```

## Quick Start

```python
import cryptohftdata as chd

# Get kline/candlestick data
klines = chd.get_klines("BTCUSDT", chd.exchanges.BINANCE_FUTURES, "2025-01-01", "2025-02-01")

# Get orderbook data
orderbook = chd.get_orderbook("ETHUSDT", chd.exchanges.BYBIT_SPOT, "2025-01-01", "2025-02-01")

# Get trade data
trades = chd.get_trades("BTCUSDT", chd.exchanges.BINANCE_SPOT, "2025-01-01", "2025-01-02")

# All methods return pandas DataFrames ready for analysis
print(klines.head())
print(f"Average price: ${klines['close'].mean():.2f}")
```

## Features

- **Simple API**: Clean and intuitive interface for accessing cryptocurrency market data
- **Direct pandas Integration**: All methods return pandas DataFrames ready for analysis
- **Parquet Support**: Efficient data transfer using parquet files for large datasets
- **Multiple Exchanges**: Support for Binance, Bybit, Kraken and OKX (both spot and futures markets)
- **Multiple Data Types**: Access to klines, orderbook, trades, ticker, mark price, funding rates, open interest, and liquidations data
- **High Performance**: Optimized for handling large datasets efficiently with pandas and pyarrow
- **Type Safety**: Full type hints for better IDE support and code quality
- **Async Support**: Both synchronous and asynchronous APIs available
- **Flexible Date Handling**: Support for various date formats and timezones

## Supported Exchanges

- Binance (Spot & Futures)
- Bybit (Spot & Futures)
- Kraken (Spot & Derivatives)
- OKX (Spot & Futures)

_More exchanges coming soon..._

## Documentation

Full documentation is available at [cryptohftdata.com/docs](https://cryptohftdata.com/docs)

## Examples

See the [examples](examples/) directory for more detailed usage examples.

## Development

### Setting up the development environment

```bash
git clone https://github.com/cryptohftdata/sdk.git
cd sdk/python
pip install -e ".[dev]"
```

### Running tests

To run the test suite, navigate to the `sdk/python` directory and use one of the following commands:

Using `pytest` (recommended):

```bash
pytest
```

This command will automatically use the configurations specified in `pyproject.toml`, including test paths and coverage options.

If you need to target a specific test file or directory, you can do so, but be mindful of the `addopts` in `pyproject.toml`:

```bash
pytest tests/test_client.py
```

If you don't have `pytest` or prefer to use the built-in `unittest` module:

```bash
python -m unittest discover tests
```

Make sure you have an active virtual environment with development dependencies installed. Some tests might require a `CRYPTOHFTDATA_API_KEY` environment variable to be set for tests that interact with the live API.

### Code formatting

```bash
black cryptohftdata tests
isort cryptohftdata tests
```

### Type checking

```bash
mypy cryptohftdata
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- Documentation: [cryptohftdata.com/docs](https://cryptohftdata.com/docs)
- Issues: [GitHub Issues](https://github.com/cryptohftdata/sdk/issues)
- Email: support@cryptohftdata.com
