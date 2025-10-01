"""
RiskOptimix - A simple Python toolkit for algorithmic trading
"""

__version__ = "0.1.0"
__author__ = "Thomas van der Hulst"
__email__ = "riskoptimix@gmail.com"

# Import main functions for easy access
from .data import get_data
from .exceptions import RiskOptimixError

__all__ = ["get_data", "RiskOptimixError"]
