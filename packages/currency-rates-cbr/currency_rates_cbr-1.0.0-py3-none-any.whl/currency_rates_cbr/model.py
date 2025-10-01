import requests
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional
from datetime import datetime, date


class CurrencyRates:
    """
    Model class for fetching currency rates from Central Bank of Russia
    Implements Singleton pattern
    """
    _instance = None
    _BASE_URL = "https://www.cbr.ru/scripts/XML_daily.asp"

    def __new__(cls, tracked_currencies: List[str] = None):
        if cls._instance is None:
            cls._instance = super(CurrencyRates, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, tracked_currencies: List[str] = None):
        if not self._initialized:
            self._tracked_currencies = tracked_currencies or ["USD", "EUR", "GBP"]
            self._rates: Dict[str, float] = {}
            self._last_update: Optional[datetime] = None
            self._initialized = True

    def _fetch_rates(self) -> None:
        """Fetch rates from CBR website"""
        try:
            response = requests.get(self._BASE_URL, params={"date_req": date.today().strftime("%d/%m/%Y")})
            response.raise_for_status()

            root = ET.fromstring(response.content)
            self._rates.clear()

            for valute in root.findall('Valute'):
                char_code = valute.find('CharCode').text
                if char_code in self._tracked_currencies:
                    value = float(valute.find('Value').text.replace(',', '.'))
                    nominal = int(valute.find('Nominal').text)
                    self._rates[char_code] = value / nominal

            self._last_update = datetime.now()

        except Exception as e:
            raise Exception(f"Failed to fetch currency rates: {e}")

    @property
    def rates(self) -> Dict[str, float]:
        """Get current currency rates"""
        if not self._rates or not self._last_update or (datetime.now() - self._last_update).seconds > 3600:
            self._fetch_rates()
        return self._rates.copy()

    @property
    def tracked_currencies(self) -> List[str]:
        """Get list of tracked currencies"""
        return self._tracked_currencies.copy()

    @tracked_currencies.setter
    def tracked_currencies(self, currencies: List[str]) -> None:
        """Set list of tracked currencies"""
        if not isinstance(currencies, list) or not all(isinstance(c, str) and len(c) == 3 for c in currencies):
            raise ValueError("Currencies must be a list of 3-character strings")
        self._tracked_currencies = currencies
        self._rates.clear()  # Clear cached rates

    def get_rate(self, currency: str) -> Optional[float]:
        """Get specific currency rate"""
        return self.rates.get(currency.upper())