"""
Database setup and helper functions for TaskFlow.

SQLite is used because it is built into Python and does not require a
separate database server. This means the app works without external files,
APIs or database setup.
"""

import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "taskflow.db"


def get_db_connection():
    """
    Create and return a SQLite database connection.

    sqlite3.Row lets us access database fields by column name, for example:
        task["title"]
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Create the tasks table if it does not already exist.

    The app calls this when it starts. Existing data is not deleted because
    the SQL uses CREATE TABLE IF NOT EXISTS.
    """
    conn = get_db_connection()

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            category TEXT NOT NULL DEFAULT 'General',
            priority TEXT NOT NULL DEFAULT 'Medium',
            status TEXT NOT NULL DEFAULT 'To Do',
            due_date TEXT,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            completed_at TEXT
        )
        """
    )

    conn.commit()
    conn.close()
