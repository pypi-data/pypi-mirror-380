import unittest
from currency_rates_cbr import CurrencyRates


class TestCurrencyRates(unittest.TestCase):
    def test_singleton_pattern(self):
        instance1 = CurrencyRates(["USD", "EUR"])
        instance2 = CurrencyRates(["GBP", "JPY"])

        self.assertIs(instance1, instance2)


if __name__ == "__main__":
    unittest.main()