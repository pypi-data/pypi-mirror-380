from typing import Dict
import json


class CurrencyView:
    """View for displaying currency rates"""

    @staticmethod
    def display_rates(rates: Dict[str, float]) -> str:
        """Display rates in formatted string"""
        if not rates:
            return "No rates available"

        output = "Current Currency Rates:\n"
        output += "-" * 30 + "\n"
        for currency, rate in rates.items():
            output += f"{currency}: {rate:.4f} RUB\n"
        return output

    @staticmethod
    def display_json(rates: Dict[str, float]) -> str:
        """Display rates as JSON"""
        return json.dumps(rates, indent=2)

    @staticmethod
    def display_html(rates: Dict[str, float]) -> str:
        """Display rates as HTML"""
        if not rates:
            return "<p>No rates available</p>"

        html = "<table border='1'><tr><th>Currency</th><th>Rate (RUB)</th></tr>"
        for currency, rate in rates.items():
            html += f"<tr><td>{currency}</td><td>{rate:.4f}</td></tr>"
        html += "</table>"
        return html