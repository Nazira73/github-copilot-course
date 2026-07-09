"""
Expense Tracker user interface.
"""

import customtkinter as ctk
from tkinter import ttk, messagebox

from expense import Expense
from expense_service import ExpenseService


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class ExpenseUI:
    """Graphical user interface for the Expense Tracker."""

    def __init__(self):

        self.service = ExpenseService()
        self.selected_expense_id = None

        self.root = ctk.CTk()
        self.root.title("Expense Tracker")
        self.root.geometry("1100x700")

        self.create_widgets()
        self.load_expenses()

    def create_widgets(self):

        title = ctk.CTkLabel(
            self.root,
            text="Expense Tracker",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=15)

        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        left_frame = ctk.CTkFrame(main_frame, width=300)
        left_frame.pack(
            side="left",
            fill="y",
            padx=10,
            pady=10
        )

        right_frame = ctk.CTkFrame(main_frame)
        right_frame.pack(
            side="right",
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        ctk.CTkLabel(
            left_frame,
            text="Title"
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 5)
        )

        self.title_entry = ctk.CTkEntry(
            left_frame,
            width=240
        )

        self.title_entry.pack(padx=20)

        ctk.CTkLabel(
            left_frame,
            text="Category"
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        self.category_combo = ctk.CTkComboBox(
            left_frame,
            width=240,
            values=[
                "Food",
                "Travel",
                "Technology",
                "Utilities",
                "Entertainment",
                "Health",
                "Education",
                "Shopping",
                "Other"
            ]
        )

        self.category_combo.pack(padx=20)
        self.category_combo.set("Food")

        ctk.CTkLabel(
            left_frame,
            text="Amount"
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        self.amount_entry = ctk.CTkEntry(
            left_frame,
            width=240
        )

        self.amount_entry.pack(padx=20)

        ctk.CTkLabel(
            left_frame,
            text="Expense Date (YYYY-MM-DD)"
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        self.date_entry = ctk.CTkEntry(
            left_frame,
            width=240
        )

        self.date_entry.pack(padx=20)

        ctk.CTkButton(
            left_frame,
            text="Add Expense",
            command=self.add_expense
        ).pack(
            fill="x",
            padx=20,
            pady=(25, 8)
        )

        ctk.CTkButton(
            left_frame,
            text="Update Expense",
            command=self.update_expense
        ).pack(
            fill="x",
            padx=20,
            pady=8
        )

        ctk.CTkButton(
            left_frame,
            text="Delete Expense",
            command=self.delete_expense
        ).pack(
            fill="x",
            padx=20,
            pady=8
        )

        ctk.CTkButton(
            left_frame,
            text="Search",
            command=self.search_expenses
        ).pack(
            fill="x",
            padx=20,
            pady=8
        )

        ctk.CTkButton(
            left_frame,
            text="Monthly Summary",
            command=self.show_summary
        ).pack(
            fill="x",
            padx=20,
            pady=8
        )

        ctk.CTkButton(
            left_frame,
            text="Clear",
            command=self.clear_fields
        ).pack(
            fill="x",
            padx=20,
            pady=8
        )

        # -----------------------------
        # Treeview Style
        # -----------------------------
        style = ttk.Style()

        style.configure(
            "Treeview",
            font=("Segoe UI", 12),
            rowheight=30
        )

        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 12, "bold")
        )

        columns = (
            "ID",
            "Title",
            "Category",
            "Amount",
            "Date"
        )

        self.tree = ttk.Treeview(
            right_frame,
            columns=columns,
            show="headings",
            height=24
        )

        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, anchor="center")

        self.tree.column("ID", width=60)
        self.tree.column("Title", width=220)
        self.tree.column("Category", width=140)
        self.tree.column("Amount", width=120)
        self.tree.column("Date", width=140)

        scrollbar = ttk.Scrollbar(
            right_frame,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.tree.pack(
            side="left",
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        scrollbar.pack(
            side="right",
            fill="y",
            pady=15
        )

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.on_row_select
        )


    def load_expenses(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        expenses = self.service.get_all_expenses()

        for expense in expenses:
            self.tree.insert(
                "",
                "end",
                values=(
                    expense.id,
                    expense.title,
                    expense.category,
                    expense.amount,
                    expense.expense_date
                )
            )

    def add_expense(self):

        try:

            expense = Expense(
                title=self.title_entry.get(),
                category=self.category_combo.get(),
                amount=float(self.amount_entry.get()),
                expense_date=self.date_entry.get()
            )

            self.service.add_expense(expense)

            messagebox.showinfo(
                "Success",
                "Expense added successfully."
            )

            self.clear_fields()
            self.load_expenses()

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    def update_expense(self):

        if self.selected_expense_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select an expense."
            )

            return

        try:

            expense = Expense(
                expense_id=self.selected_expense_id,
                title=self.title_entry.get(),
                category=self.category_combo.get(),
                amount=float(self.amount_entry.get()),
                expense_date=self.date_entry.get()
            )

            self.service.update_expense(expense)

            messagebox.showinfo(
                "Success",
                "Expense updated successfully."
            )

            self.clear_fields()
            self.load_expenses()

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    def delete_expense(self):

        if self.selected_expense_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select an expense."
            )

            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Delete selected expense?"
        )

        if not confirm:
            return

        self.service.delete_expense(
            self.selected_expense_id
        )

        self.clear_fields()
        self.load_expenses()

    def search_expenses(self):

        keyword = self.title_entry.get()

        expenses = self.service.search_expenses(keyword)

        for item in self.tree.get_children():
            self.tree.delete(item)

        for expense in expenses:

            self.tree.insert(
                "",
                "end",
                values=(
                    expense.id,
                    expense.title,
                    expense.category,
                    expense.amount,
                    expense.expense_date
                )
            )

    def show_summary(self):

        summary = self.service.monthly_summary()

        message = ""

        for category, total in summary:

            message += f"{category}: ₹{total}\n"

        messagebox.showinfo(
            "Monthly Summary",
            message
        )

    def clear_fields(self):

        self.selected_expense_id = None

        self.title_entry.delete(0, "end")
        self.amount_entry.delete(0, "end")
        self.date_entry.delete(0, "end")

        self.category_combo.set("Food")

        self.load_expenses()

    def on_row_select(self, event):

        selected = self.tree.focus()

        if not selected:
            return

        values = self.tree.item(
            selected,
            "values"
        )


        self.title_entry.delete(0, "end")
        self.amount_entry.delete(0, "end")
        self.date_entry.delete(0, "end")

        self.selected_expense_id = int(values[0])

        self.title_entry.insert(
            0,
            values[1]
        )

        self.category_combo.set(
            values[2]
        )

        self.amount_entry.insert(
            0,
            values[3]
        )

        self.date_entry.insert(
            0,
            values[4]
        )

    def run(self):
        """Start the application."""

        self.root.mainloop()