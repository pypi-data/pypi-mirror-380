import unittest
import os
from currency_rates_cbr import CurrencyController


class TestCurrencyController(unittest.TestCase):
    def setUp(self):
        self.controller = CurrencyController(["USD", "EUR"], ":memory:")

    def test_initialization(self):
        self.assertEqual(self.controller.model.tracked_currencies, ["USD", "EUR"])

    def test_update_currencies(self):
        self.controller.update_tracked_currencies(["GBP", "JPY"])
        self.assertEqual(self.controller.model.tracked_currencies, ["GBP", "JPY"])


if __name__ == "__main__":
    unittest.main()