import csv
import os

# File path for income CSV file
FILE_PATH = r'C:/Users/antim/OneDrive/Documents/GitHub/ThinkTrack/budget/income/Income.csv'

def append_csv_row(row):
    """
    Appends a single income row to the CSV file.
    Creates the file with a header if it doesn't exist.
    """
    file_exists = os.path.isfile(FILE_PATH)
    
    with open(FILE_PATH, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Date', 'Amount', 'Category', 'Account', 'Note', 'Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header if the file is new
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(row)
        print("Income added successfully to CSV.")

def main():
    print("Enter a new income:")
    date = input("Date (YYYY-MM-DD): ")
    amount = input("Amount: ")
    category = input("Category: ")
    account = input("Account: ")
    note = input("Note: ")
    description = input("Description: ")
    
    income = {
        'Date': date,
        'Amount': amount,
        'Category': category,
        'Account': account,
        'Note': note,
        'Description': description
    }
    
    append_csv_row(income)

if __name__ == '__main__':
    main()
# This script allows the user to input income details and appends them to a CSV file.
# It creates the file with a header if it doesn't exist.