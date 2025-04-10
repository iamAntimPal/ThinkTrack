# ui/forms.py
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from app.manager import BudgetManager

class EntryForm(tk.Frame):
    """
    Form for adding or editing an income/expense entry.
    """
    def __init__(self, master, user, on_submit, **kwargs):
        super().__init__(master, **kwargs)
        self.user = user
        self.on_submit = on_submit
        self.manager = BudgetManager()
        self.build_form()

    def build_form(self):
        tk.Label(self, text="Add/Edit Entry", font=('Arial', 14)).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Type selection
        tk.Label(self, text="Type:").grid(row=1, column=0, sticky='e')
        self.type_var = tk.StringVar(value="expense")
        tk.OptionMenu(self, self.type_var, "income", "expense").grid(row=1, column=1, sticky='w', padx=5)
        
        # Amount entry
        tk.Label(self, text="Amount:").grid(row=2, column=0, sticky='e')
        self.amount_entry = tk.Entry(self)
        self.amount_entry.grid(row=2, column=1, sticky='w', padx=5)
        
        # Category entry
        tk.Label(self, text="Category:").grid(row=3, column=0, sticky='e')
        self.category_entry = tk.Entry(self)
        self.category_entry.grid(row=3, column=1, sticky='w', padx=5)
        
        # Date selection
        tk.Label(self, text="Date:").grid(row=4, column=0, sticky='e')
        self.date_entry = DateEntry(self)
        self.date_entry.grid(row=4, column=1, sticky='w', padx=5)
        
        # Description entry
        tk.Label(self, text="Description:").grid(row=5, column=0, sticky='e')
        self.desc_entry = tk.Entry(self)
        self.desc_entry.grid(row=5, column=1, sticky='w', padx=5)
        
        # Submit button
        tk.Button(self, text="Submit", command=self.submit_form).grid(row=6, column=0, columnspan=2, pady=10)

    def submit_form(self):
        try:
            entry_type = self.type_var.get()
            amount = float(self.amount_entry.get())
            category = self.category_entry.get()
            date = self.date_entry.get_date().strftime('%Y-%m-%d')
            description = self.desc_entry.get()
            # Add entry using the business logic
            self.manager.add_entry(self.user['id'], entry_type, amount,
                                   self.user['currency'], category, date, description)
            messagebox.showinfo("Success", "Entry added successfully!")
            self.on_submit()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add entry: {e}")
