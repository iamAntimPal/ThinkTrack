# data/models.py

class Entry:
    """
    Data model for income/expense entries.
    """
    def __init__(self, user_id, entry_type, amount, currency, category, date, description):
        self.user_id = user_id
        self.entry_type = entry_type  # "income" or "expense"
        self.amount = amount
        self.currency = currency
        self.category = category
        self.date = date
        self.description = description

class RecurringTransaction:
    """
    Data model for recurring transactions.
    """
    def __init__(self, user_id, entry_type, amount, currency, category, frequency, start_date, end_date, last_occurrence):
        self.user_id = user_id
        self.entry_type = entry_type
        self.amount = amount
        self.currency = currency
        self.category = category
        self.frequency = frequency  # e.g., "daily", "weekly", "monthly"
        self.start_date = start_date
        self.end_date = end_date
        self.last_occurrence = last_occurrence
