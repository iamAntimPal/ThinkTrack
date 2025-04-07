import csv
import os

def append_csv_row(file_path, row):
    """
    Appends a single expense row to a CSV file.
    If the file does not exist, it creates one with a header.
    """
    # Check if the file already exists
    file_exists = os.path.isfile(file_path)
    
    # Open file in append mode
    with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
        # Define the header fields
        fieldnames = ['Date', 'Amount', 'Category', 'Account', 'Note', 'Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header if file is new
        if not file_exists:
            writer.writeheader()
            
        writer.writerow(row)
        print("CSV row appended successfully.")

def append_markdown_entry(file_path, entry_text):
    """
    Appends a text entry to a Markdown file.
    """
    with open(file_path, 'a', encoding='utf-8') as mdfile:
        # Append a newline if needed and write the new entry
        mdfile.write("\n" + entry_text + "\n")
        print("Markdown entry appended successfully.")

if __name__ == '__main__':
    # --- Example: Append new expense to CSV ---
    new_expense = {
        'Date': '2025-04-08',
        'Amount': '75',
        'Category': 'Utilities',
        'Account': 'Debit Card',
        'Note': 'Electricity bill',
        'Description': 'Monthly electricity payment'
    }
    csv_file = 'expenses.csv'
    append_csv_row(csv_file, new_expense)
    
    # --- Example: Append a new Markdown expense entry ---
    new_md_entry = (
        "# Daily Expense Log - 2025-04-08\n\n"
        "## Expenses\n\n"
        "| Date       | Amount | Category  | Account    | Note            | Description                |\n"
        "|------------|--------|-----------|------------|-----------------|----------------------------|\n"
        "| 2025-04-08 | $75    | Utilities | Debit Card | Electricity bill| Monthly electricity payment|\n\n"
        "### Notes:\n"
        "- Add additional expenses as needed."
    )
    md_file = 'expenses.md'
    append_markdown_entry(md_file, new_md_entry)
