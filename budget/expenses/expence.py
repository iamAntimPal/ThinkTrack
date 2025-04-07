import csv
import os

CSV_FILE = r'C:/Users/antim/OneDrive/Documents/GitHub/ThinkTrack/budget/expenses/Expense.csv'

def append_csv_row(row):
    """
    Appends a single expense row to the CSV file.
    Creates the file with a header if it doesn't exist.
    """
    file_exists = os.path.isfile(CSV_FILE)
    
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Date', 'Amount', 'Category', 'Account', 'Note', 'Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(row)
        print("Expense added successfully to CSV.")

def main():
    print("Enter a new expense:")
    date = input("Date (YYYY-MM-DD): ")
    amount = input("Amount: ")
    category = input("Category: ")
    account = input("Account: ")
    note = input("Note: ")
    description = input("Description: ")
    
    expense = {
        'Date': date,
        'Amount': amount,
        'Category': category,
        'Account': account,
        'Note': note,
        'Description': description
    }
    
    append_csv_row(expense)

if __name__ == '__main__':
    main()
