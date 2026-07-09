"""
Unit tests for ExpenseService.
"""

from expense_service import ExpenseService


class TestExpenseService:
    """Unit tests for ExpenseService."""

    def setup_method(self):
        """Create a fresh ExpenseService instance before each test."""
        self.service = ExpenseService()