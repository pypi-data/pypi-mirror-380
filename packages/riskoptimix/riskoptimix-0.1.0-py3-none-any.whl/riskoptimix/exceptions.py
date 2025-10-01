"""Custom exceptions for RiskOptimix"""


class RiskOptimixError(Exception):
    """Base exception for all RiskOptimix errors"""

    pass


class DataError(RiskOptimixError):
    """Raised when data cannot be fetched or is invalid"""

    pass


class ValidationError(RiskOptimixError):
    """Raised when input validation fails"""

    pass


class BacktestError(RiskOptimixError):
    """Raised when backtest encounters an error"""

    pass


class UserError(RiskOptimixError):
    """Raised when user input is invalid"""

    pass
