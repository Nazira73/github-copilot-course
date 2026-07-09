# Expense Tracker – GitHub Copilot Demo Project

## Overview

This project is a simple Expense Tracker application built using **Python**, **MySQL**, and **CustomTkinter**.

It is designed specifically for the **GitHub Copilot Hands-on Workshop**. The application serves as the sample project used throughout the workshop to demonstrate GitHub Copilot features such as Workspace, Prompting, Custom Instructions, Planning Mode, Agent Mode, Agent Skills, Cost Management, and an end-to-end development workflow.

---

## Prerequisites

Before running the application, ensure the following software is installed:

* Python 3.10 or later
* MySQL Server 8.0 or later
* Git
* Visual Studio Code
* GitHub Copilot extension
* GitHub Copilot Chat extension

---

## Clone the Repository

```bash
git clone <repository-url>
cd expense_tracker
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure the Database

Copy the example environment file.

### Windows

```bash
copy .env.example .env
```

### macOS / Linux

```bash
cp .env.example .env
```

Open the `.env` file and update the database credentials.

```text
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=expense_tracker
```

---

## Run the Application

```bash
python main.py
```

On the first run, the application automatically:

* Creates the `expense_tracker` database (if it does not exist)
* Creates the required tables
* Loads sample data (only if the database is empty)
* Launches the Expense Tracker application

No additional setup is required.

---

## Project Structure

```
expense_tracker/
│
├── config.py
├── database.py
├── expense.py
├── expense_service.py
├── main.py
├── setup_database.py
├── ui.py
│
├── schema.sql
├── sample_data.sql
│
├── requirements.txt
├── .env.example
└── README.md
```

---

## Technologies Used

* Python
* MySQL
* CustomTkinter
* Pytest
* python-dotenv

---

## Troubleshooting

### MySQL connection error

Verify the values in the `.env` file and ensure the MySQL server is running.

### Module not found

Install the project dependencies again.

```bash
pip install -r requirements.txt
```

### Permission denied

Ensure the MySQL user has permission to create databases and tables.

---

## Workshop Notes

This repository is intentionally kept simple to provide a clean environment for learning GitHub Copilot. During the workshop, participants will use this project to explore and practice various GitHub Copilot features while implementing enhancements and improvements.

Happy Coding!
