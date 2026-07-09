"""
Expense service.

Provides business operations for managing expenses in the
Expense Tracker application.
"""

from database import Database
from expense import Expense


class ExpenseService:
    """Provides CRUD operations for expenses."""

    def add_expense(self, expense):
        """Add a new expense to the database."""

        connection = Database.get_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO expenses
        (
            title,
            category,
            amount,
            expense_date
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s
        )
        """

        cursor.execute(
            query,
            (
                expense.title,
                expense.category,
                expense.amount,
                expense.expense_date
            )
        )

        connection.commit()

        cursor.close()
        connection.close()

    def get_all_expenses(self):
        """Return all expenses ordered by date."""

        connection = Database.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                title,
                category,
                amount,
                expense_date
            FROM expenses
            ORDER BY expense_date DESC
            """
        )

        rows = cursor.fetchall()

        expenses = []

        for row in rows:
            expenses.append(
                Expense(
                    expense_id=row[0],
                    title=row[1],
                    category=row[2],
                    amount=row[3],
                    expense_date=row[4]
                )
            )

        cursor.close()
        connection.close()

        return expenses

    def get_expense_by_id(self, expense_id):
        """Return a single expense by its ID."""

        connection = Database.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                title,
                category,
                amount,
                expense_date
            FROM expenses
            WHERE id = %s
            """,
            (expense_id,)
        )

        row = cursor.fetchone()

        cursor.close()
        connection.close()

        if row:
            return Expense(
                expense_id=row[0],
                title=row[1],
                category=row[2],
                amount=row[3],
                expense_date=row[4]
            )

        return None

    def update_expense(self, expense):
        """Update an existing expense."""

        connection = Database.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE expenses
            SET
                title=%s,
                category=%s,
                amount=%s,
                expense_date=%s
            WHERE id=%s
            """,
            (
                expense.title,
                expense.category,
                expense.amount,
                expense.expense_date,
                expense.id
            )
        )

        connection.commit()

        cursor.close()
        connection.close()

    def delete_expense(self, expense_id):
        """Delete an expense by its ID."""

        connection = Database.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM expenses
            WHERE id=%s
            """,
            (expense_id,)
        )

        connection.commit()

        cursor.close()
        connection.close()

    def search_expenses(self, search_text):
        """Search expenses by title or category."""

        connection = Database.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                title,
                category,
                amount,
                expense_date
            FROM expenses
            WHERE
                title LIKE %s
                OR category LIKE %s
            ORDER BY expense_date DESC
            """,
            (
                f"%{search_text}%",
                f"%{search_text}%"
            )
        )

        rows = cursor.fetchall()

        expenses = []

        for row in rows:
            expenses.append(
                Expense(
                    expense_id=row[0],
                    title=row[1],
                    category=row[2],
                    amount=row[3],
                    expense_date=row[4]
                )
            )

        cursor.close()
        connection.close()

        return expenses

    def monthly_summary(self):
        """Return the total expense amount grouped by category."""

        connection = Database.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                category,
                SUM(amount)
            FROM expenses
            GROUP BY category
            ORDER BY SUM(amount) DESC
            """
        )

        summary = cursor.fetchall()

        cursor.close()
        connection.close()

        return summary
    