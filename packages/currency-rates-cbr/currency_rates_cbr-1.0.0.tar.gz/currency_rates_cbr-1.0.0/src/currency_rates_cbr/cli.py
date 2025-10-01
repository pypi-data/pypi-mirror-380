#!/usr/bin/env python3
"""
CLI interface for currency-rates-cbr
"""

import argparse
from .controller import CurrencyController
from .view import CurrencyView


def main():
    parser = argparse.ArgumentParser(description="Fetch currency rates from Central Bank of Russia")
    parser.add_argument(
        "-c", "--currencies",
        nargs="+",
        default=["USD", "EUR", "GBP"],
        help="List of currencies to track (default: USD EUR GBP)"
    )
    parser.add_argument(
        "-f", "--format",
        choices=["text", "json", "html"],
        default="text",
        help="Output format (default: text)"
    )
    parser.add_argument(
        "--db-path",
        default="currency_rates.db",
        help="Path to SQLite database (default: currency_rates.db)"
    )

    args = parser.parse_args()

    try:
        # Initialize controller
        controller = CurrencyController(args.currencies, args.db_path)

        # Get current rates
        rates = controller.get_current_rates()

        # Display in requested format
        if args.format == "text":
            print(CurrencyView.display_rates(rates))
        elif args.format == "json":
            print(CurrencyView.display_json(rates))
        elif args.format == "html":
            print(CurrencyView.display_html(rates))

    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())