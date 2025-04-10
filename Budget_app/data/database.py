# data/database.py
import sqlite3
import os
from data.models import Entry, RecurringTransaction

DB_PATH = 'budget_app.db'

class Database:
    """
    SQLite Database operations encapsulated in a class.
    """
    @staticmethod
    def get_connection():
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn

    @staticmethod
    def initialize_db():
        """
        Create tables if they don’t exist.
        """
        conn = Database.get_connection()
        cursor = conn.cursor()
        # Create users table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash BLOB NOT NULL,
            currency TEXT NOT NULL DEFAULT 'USD'
        )
        ''')

        # Create entries table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            currency TEXT NOT NULL,
            category TEXT,
            date TEXT NOT NULL,
            description TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        ''')

        # Create recurring transactions table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS recurring (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            currency TEXT NOT NULL,
            category TEXT,
            frequency TEXT NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT,
            last_occurrence TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        ''')

        conn.commit()
        conn.close()

    # --- User Operations ---
    @staticmethod
    def create_user(username: str, password_hash: bytes, currency: str):
        conn = Database.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO users (username, password_hash, currency)
        VALUES (?, ?, ?)
        ''', (username, password_hash, currency))
        conn.commit()
        conn.close()

    @staticmethod
    def get_user_by_username(username: str):
        conn = Database.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM users WHERE username = ?
        ''', (username,))
        user = cursor.fetchone()
        conn.close()
        return user

    # --- Entry Operations ---
    @staticmethod
    def insert_entry(entry: Entry):
        conn = Database.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO entries (user_id, type, amount, currency, category, date, description)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (entry.user_id, entry.entry_type, entry.amount, entry.currency,
              entry.category, entry.date, entry.description))
        conn.commit()
        last_id = cursor.lastrowid
        conn.close()
        return last_id

    @staticmethod
    def update_entry(entry_id: int, **kwargs):
        conn = Database.get_connection()
        cursor = conn.cursor()
        fields = []
        values = []
        for key, value in kwargs.items():
            fields.append(f"{key} = ?")
            values.append(value)
        values.append(entry_id)
        cursor.execute(f'''
        UPDATE entries SET {', '.join(fields)} WHERE id = ?
        ''', tuple(values))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_entry(entry_id: int):
        conn = Database.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM entries WHERE id = ?', (entry_id,))
        conn.commit()
        conn.close()

    # --- Recurring Transactions Operations ---
    @staticmethod
    def insert_recurring(recurring: RecurringTransaction):
        conn = Database.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO recurring (user_id, type, amount, currency, category, frequency, start_date, end_date, last_occurrence)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (recurring.user_id, recurring.entry_type, recurring.amount, recurring.currency,
              recurring.category, recurring.frequency, recurring.start_date, recurring.end_date, recurring.last_occurrence))
        conn.commit()
        last_id = cursor.lastrowid
        conn.close()
        return last_id

    @staticmethod
    def get_all_recurring():
        conn = Database.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM recurring')
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    @staticmethod
    def update_recurring_last_occurrence(recurring_id: int, new_date: str):
        conn = Database.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE recurring SET last_occurrence = ? WHERE id = ?
        ''', (new_date, recurring_id))
        conn.commit()
        conn.close()

    @staticmethod
    def insert_entry_from_recurring(recurring: dict):
        from datetime import datetime
        entry = Entry(
            user_id=recurring['user_id'],
            entry_type=recurring['type'],
            amount=recurring['amount'],
            currency=recurring['currency'],
            category=recurring['category'],
            date=datetime.today().strftime('%Y-%m-%d'),
            description='Recurring transaction'
        )
        return Database.insert_entry(entry)
