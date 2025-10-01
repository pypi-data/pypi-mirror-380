import unittest
from currency_rates_cbr import CurrencyView


class TestCurrencyView(unittest.TestCase):
    def test_display_rates(self):
        rates = {"USD": 75.5, "EUR": 85.2}
        result = CurrencyView.display_rates(rates)
        self.assertIn("USD", result)
        self.assertIn("75.5000", result)

    def test_display_json(self):
        rates = {"USD": 75.5, "EUR": 85.2}
        result = CurrencyView.display_json(rates)
        self.assertIn('"USD": 75.5', result)


if __name__ == "__main__":
    unittest.main()