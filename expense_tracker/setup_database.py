"""
Database setup utility.

Creates the Expense Tracker database, builds the schema,
and loads sample data.
"""

import mysql.connector

from config import DB_CONFIG


def create_database():
    """Create the Expense Tracker database if it does not already exist."""

    connection = mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )

    cursor = connection.cursor()

    cursor.execute(
        f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}"
    )

    cursor.close()
    connection.close()


def execute_sql_file(sql_file):
    """Execute all SQL statements from the specified SQL file."""

    connection = mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        database=DB_CONFIG["database"]
    )

    cursor = connection.cursor()

    with open(sql_file, "r") as file:
        sql_script = file.read()

    commands = sql_script.split(";")

    for command in commands:
        if command.strip():
            cursor.execute(command)

    connection.commit()

    cursor.close()
    connection.close()


def is_database_empty():
    """Return True if the expenses table contains no records."""

    connection = mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        database=DB_CONFIG["database"]
    )

    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM expenses"
    )

    count = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return count == 0


def setup_database():
    """Initialize the database schema and load sample data."""

    print("Creating database...")
    create_database()

    print("Creating tables...")
    execute_sql_file("schema.sql")

    if is_database_empty():

        print("Loading sample data...")
        execute_sql_file("sample_data.sql")

    else:

        print("Sample data already exists. Skipping.")

    print("Database setup completed.")


if __name__ == "__main__":
    setup_database()