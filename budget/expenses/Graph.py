import csv
import os
import tkinter as tk
from tkinter import messagebox
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

CSV_FILE = r'C:/Users/antim/OneDrive/Documents/GitHub/ThinkTrack/budget/expenses/Expense.csv'

def append_csv_row(row):
    file_exists = os.path.isfile(CSV_FILE)
    
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Date', 'Amount', 'Category', 'Account', 'Note', 'Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(row)
        print("Expense added successfully to CSV.")

def plot_expenses():
    categories = []
    amounts = []

    with open(CSV_FILE, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        category_sums = {}
        for row in reader:
            category = row['Category']
            amount = float(row['Amount'])
            category_sums[category] = category_sums.get(category, 0) + amount

        for cat, amt in category_sums.items():
            categories.append(cat)
            amounts.append(amt)

    fig, ax = plt.subplots()
    ax.pie(amounts, labels=categories, autoppt='%1.1f%%')
    ax.set_title('Expense Distribution by Category')
    plt.show()

class ExpenseTrackerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Expense Tracker")
        self.geometry("400x300")

        fields = ['Date', 'Amount', 'Category', 'Account', 'Note', 'Description']
        self.entries = []

        for idx, label_text in enumerate(fields):
            label = tk.Label(self, text=label_text)
            label.grid(row=idx, column=0, sticky=tk.W, padx=10, pady=5)
            entry = tk.Entry(self)
            entry.grid(row=idx, column=1, padx=10, pady=5)
            self.entries.append(entry)

        submit_btn = tk.Button(self, text="Add Expense", command=self.add_expense)
        submit_btn.grid(row=len(fields), column=0, pady=10)

        graph_btn = tk.Button(self, text="Show Expense Graph", command=self.show_graph)
        graph_btn.grid(row=len(fields), column=1, pady=10)

        # Bind Enter key to add_expense
        self.bind('<Return>', lambda e: self.add_expense())

    def add_expense(self, *args):
        new_row = {
            'Date': self.entries[0].get(),
            'Amount': self.entries[1].get(),
            'Category': self.entries[2].get(),
            'Account': self.entries[3].get(),
            'Note': self.entries[4].get(),
            'Description': self.entries[5].get()
        }
        append_csv_row(new_row)
        messagebox.showinfo("Success", "Expense added!")

        # Clear all input fields after submission
        for entry in self.entries:
            entry.delete(0, tk.END)

    def show_graph(self):
        plot_expenses()

if __name__ == '__main__':
    app = ExpenseTrackerGUI()
    app.mainloop()
# This code is a simple expense tracker GUI application using Tkinter and Matplotlib.