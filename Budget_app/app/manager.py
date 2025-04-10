# app/manager.py
from data.database import Database
from data.models import Entry, RecurringTransaction
import datetime

class BudgetManager:
    """
    Contains business logic for managing income/expense entries and recurring transactions.
    """
    def __init__(self):
        self.db = Database

    def add_entry(self, user_id: int, entry_type: str, amount: float, currency: str,
                  category: str, date: str, description: str):
        """
        Create a new income or expense entry.
        """
        entry = Entry(user_id, entry_type, amount, currency, category, date, description)
        return self.db.insert_entry(entry)

    def update_entry(self, entry_id: int, **kwargs):
        """
        Update an existing entry.
        """
        return self.db.update_entry(entry_id, **kwargs)

    def delete_entry(self, entry_id: int):
        """
        Delete an entry.
        """
        return self.db.delete_entry(entry_id)

    def schedule_recurring(self, user_id: int, entry_type: str, amount: float, currency: str,
                           category: str, frequency: str, start_date: str, end_date: str):
        """
        Schedule a new recurring transaction.
        """
        recurring = RecurringTransaction(user_id, entry_type, amount, currency, category,
                                         frequency, start_date, end_date, last_occurrence=start_date)
        return self.db.insert_recurring(recurring)

    def update_recurring_transactions(self):
        """
        Process all recurring transactions, and add a new entry if needed.
        (This method should be linked with a background scheduler.)
        """
        recurring_list = self.db.get_all_recurring()
        today = datetime.date.today()
        for rec in recurring_list:
            last_date = datetime.datetime.strptime(rec['last_occurrence'], '%Y-%m-%d').date()
            if rec['frequency'] == 'daily' and (today - last_date).days >= 1:
                self.db.insert_entry_from_recurring(rec)
                self.db.update_recurring_last_occurrence(rec['id'], today.strftime('%Y-%m-%d'))
            # Extend logic for 'weekly' and 'monthly' as needed.
