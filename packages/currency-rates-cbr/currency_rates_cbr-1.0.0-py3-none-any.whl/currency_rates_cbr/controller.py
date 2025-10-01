from .model import CurrencyRates
from .database import CurrencyDatabase
from typing import Dict, List


class CurrencyController:
    """Controller for managing currency rates logic"""

    def __init__(self, tracked_currencies: List[str] = None, db_path: str = "currency_rates.db"):
        self.model = CurrencyRates(tracked_currencies)
        self.database = CurrencyDatabase(db_path)

    def get_current_rates(self) -> Dict[str, float]:
        """Get current rates and save to database"""
        rates = self.model.rates
        self.database.save_rates(rates)
        return rates

    def update_tracked_currencies(self, currencies: List[str]) -> None:
        """Update list of tracked currencies"""
        self.model.tracked_currencies = currencies

    def get_historical_data(self, currency: str, days: int = 30) -> list:
        """Get historical data for a currency"""
        return self.database.get_historical_rates(currency, days)