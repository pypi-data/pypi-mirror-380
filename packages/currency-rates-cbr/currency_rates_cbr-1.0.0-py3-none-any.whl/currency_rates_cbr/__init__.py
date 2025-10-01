"""
Currency Rates CBR - A Python library for fetching currency rates from Central Bank of Russia
"""

__version__ = "1.0.0"
__author__ = "tarassiky"
__email__ = "tarasova_dasha5@mail.ru"

from .model import CurrencyRates
from .controller import CurrencyController
from .view import CurrencyView

__all__ = ["CurrencyRates", "CurrencyController", "CurrencyView"]