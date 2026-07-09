"""
Database connection helper.

Provides a single method to establish a connection to the
Expense Tracker MySQL database.
"""

import mysql.connector

from config import DB_CONFIG


class Database:
    """Utility class for creating database connections."""

    @staticmethod
    def get_connection():
        """Create and return a MySQL database connection."""
        return mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"]
        )