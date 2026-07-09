"""
Application entry point.

Starts the Expense Tracker application.
"""

from setup_database import setup_database
from ui import ExpenseUI


def main():
    """Start the Expense Tracker application."""

    setup_database()

    app = ExpenseUI()
    app.run()


if __name__ == "__main__":
    main()