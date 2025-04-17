# data/database.py
import csv
import os
from data.models import Entry, RecurringTransaction

# Define file paths
USERS_CSV = os.path.join("data", "users.csv")
ENTRIES_CSV = os.path.join("data", "entries.csv")
RECURRING_CSV = os.path.join("data", "recurring.csv")

class Database:
    """
    CSV-based database operations.
    """
    @staticmethod
    def initialize_csv_files():
        """
        Create the data folder and CSV files with headers if they do not exist.
        """
        if not os.path.exists("data"):
            os.makedirs("data")
            print("Created folder: data")
        if not os.path.isfile(USERS_CSV):
            with open(USERS_CSV, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "username", "password_hash", "currency"])
            print("Created file: users.csv")
        if not os.path.isfile(ENTRIES_CSV):
            with open(ENTRIES_CSV, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "user_id", "type", "amount", "currency", "category", "date", "description"])
            print("Created file: entries.csv")
        if not os.path.isfile(RECURRING_CSV):
            with open(RECURRING_CSV, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "user_id", "type", "amount", "currency", "category", "frequency", "start_date", "end_date", "last_occurrence"])
            print("Created file: recurring.csv")

    @staticmethod
    def _get_next_id(csv_path):
        try:
            with open(csv_path, "r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)  # skip header
                ids = [int(row[0]) for row in reader if row and row[0].isdigit()]
                return max(ids) + 1 if ids else 1
        except Exception:
            return 1

    # --- User Operations ---
    @staticmethod
    def create_user(username: str, password_hash: str, currency: str):
        user_id = Database._get_next_id(USERS_CSV)
        with open(USERS_CSV, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([user_id, username, password_hash, currency])

    @staticmethod
    def get_user_by_username(username: str):
        with open(USERS_CSV, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["username"] == username:
                    return row
        return None

    # --- Entry Operations ---
    @staticmethod
    def insert_entry(entry: Entry):
        entry_id = Database._get_next_id(ENTRIES_CSV)
        with open(ENTRIES_CSV, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([entry_id, entry.user_id, entry.entry_type, entry.amount,
                             entry.currency, entry.category, entry.date, entry.description])
        return entry_id

    @staticmethod
    def update_entry(entry_id: int, **kwargs):
        updated = False
        rows = []
        with open(ENTRIES_CSV, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if int(row["id"]) == entry_id:
                    for key, value in kwargs.items():
                        if key in row:
                            row[key] = value
                    updated = True
                rows.append(row)
        if updated:
            with open(ENTRIES_CSV, "w", newline="", encoding="utf-8") as f:
                fieldnames = ["id", "user_id", "type", "amount", "currency", "category", "date", "description"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)

    @staticmethod
    def delete_entry(entry_id: int):
        rows = []
        with open(ENTRIES_CSV, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if int(row["id"]) != entry_id:
                    rows.append(row)
        with open(ENTRIES_CSV, "w", newline="", encoding="utf-8") as f:
            fieldnames = ["id", "user_id", "type", "amount", "currency", "category", "date", "description"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    # --- Recurring Transactions Operations ---
    @staticmethod
    def insert_recurring(recurring: RecurringTransaction):
        rec_id = Database._get_next_id(RECURRING_CSV)
        with open(RECURRING_CSV, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([rec_id, recurring.user_id, recurring.entry_type, recurring.amount,
                             recurring.currency, recurring.category, recurring.frequency,
                             recurring.start_date, recurring.end_date, recurring.last_occurrence])
        return rec_id

    @staticmethod
    def get_all_recurring():
        with open(RECURRING_CSV, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return [row for row in reader]

    @staticmethod
    def update_recurring_last_occurrence(recurring_id: int, new_date: str):
        updated = False
        rows = []
        with open(RECURRING_CSV, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if int(row["id"]) == recurring_id:
                    row["last_occurrence"] = new_date
                    updated = True
                rows.append(row)
        if updated:
            with open(RECURRING_CSV, "w", newline="", encoding="utf-8") as f:
                fieldnames = ["id", "user_id", "type", "amount", "currency", "category", "frequency", "start_date", "end_date", "last_occurrence"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)

    @staticmethod
    def insert_entry_from_recurring(recurring: dict):
        from datetime import datetime
        entry = Entry(
            user_id=recurring["user_id"],
            entry_type=recurring["type"],
            amount=recurring["amount"],
            currency=recurring["currency"],
            category=recurring["category"],
            date=datetime.today().strftime("%Y-%m-%d"),
            description="Recurring transaction"
        )
        return Database.insert_entry(entry)
