"""
Expense model.

Represents a single expense record in the Expense Tracker application.
"""


class Expense:
    """Represents an expense entered by the user."""

    def __init__(
        self,
        title,
        category,
        amount,
        expense_date,
        expense_id=None
    ):
        self.id = expense_id
        self.title = title
        self.category = category
        self.amount = amount
        self.expense_date = expense_date

    def __str__(self):
        return (
            f"{self.title} | "
            f"{self.category} | "
            f"{self.amount} | "
            f"{self.expense_date}"
        )