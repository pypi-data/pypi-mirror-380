import sqlite3
from typing import Dict, List
from datetime import datetime


class CurrencyDatabase:
    """Database handler for storing currency rates"""

    def __init__(self, db_path: str = "currency_rates.db"):
        self.db_path = db_path
        self._init_database()

    def _init_database(self) -> None:
        """Initialize database tables"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS currency_rates (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    currency_code TEXT NOT NULL,
                    rate REAL NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_currency_timestamp 
                ON currency_rates(currency_code, timestamp)
            """)

    def save_rates(self, rates: Dict[str, float]) -> None:
        """Save currency rates to database"""
        with sqlite3.connect(self.db_path) as conn:
            for currency, rate in rates.items():
                conn.execute(
                    "INSERT INTO currency_rates (currency_code, rate) VALUES (?, ?)",
                    (currency, rate)
                )

    def get_historical_rates(self, currency: str, days: int = 30) -> List[tuple]:
        """Get historical rates for a currency"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("""
                SELECT rate, timestamp 
                FROM currency_rates 
                WHERE currency_code = ? 
                AND timestamp >= datetime('now', ?)
                ORDER BY timestamp DESC
            """, (currency, f'-{days} days'))
            return cursor.fetchall()