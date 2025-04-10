# app/manager.py
from data import database
from data.models import Entry, RecurringTransaction
import datetime

def add_entry(user_id: int, entry_type: str, amount: float, currency: str, 
              category: str, date: str, description: str):
    """
    Adds a new income or expense entry.
    """
    entry = Entry(user_id, entry_type, amount, currency, category, date, description)
    return database.insert_entry(entry)

def update_entry(entry_id: int, **kwargs):
    """
    Updates an existing entry.
    """
    return database.update_entry(entry_id, **kwargs)

def delete_entry(entry_id: int):
    """
    Deletes an entry.
    """
    return database.delete_entry(entry_id)

def schedule_recurring(user_id: int, entry_type: str, amount: float, currency: str, 
                         category: str, frequency: str, start_date: str, end_date: str):
    """
    Schedules a recurring transaction.
    """
    recurring = RecurringTransaction(user_id, entry_type, amount, currency, category,
                                     frequency, start_date, end_date, last_occurrence=start_date)
    return database.insert_recurring(recurring)

def update_recurring_transactions():
    """
    Check recurring transactions and add an entry if needed.
    This would be called periodically by a background scheduler.
    """
    recurring_list = database.get_all_recurring()
    today = datetime.date.today()
    for rec in recurring_list:
        last_date = datetime.datetime.strptime(rec['last_occurrence'], '%Y-%m-%d').date()
        # Based on frequency, determine if a new occurrence should be added
        if rec['frequency'] == 'daily' and (today - last_date).days >= 1:
            # Add new entry and update last occurrence date
            database.insert_entry_from_recurring(rec)
            database.update_recurring_last_occurrence(rec['id'], today.strftime('%Y-%m-%d'))
        # Similar logic for weekly and monthly can be implemented here.
