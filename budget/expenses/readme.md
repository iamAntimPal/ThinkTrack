# Expense Tracker

This repository contains Python scripts to manage and record your expense data using CSV files. The scripts allow you to create the CSV file with a header, add an initial expense record, and append new expense entries interactively.

## File Structure

- **Expense Header Setup:**  
  `expense_header_setup.py`  
  This script creates the expense CSV file with the following header if it doesn't exist:

```md
  Date,Amount,Category,Account,Note,Description
```

- **Expense Tracker:**  
  `expense_tracker.py`  
  This script lets you add new expense entries via the command line. It appends your data to the CSV file without overwriting any existing content.

- **expense.csv:**  
  `expense.csv`  
  This is the file where all expense data is stored.

## CSV File Format

The CSV file is structured with the following headers:
- **Date:** The date of the expense entry (format: YYYY-MM-DD).
- **Amount:** The amount spent.
- **Category:** The expense category (e.g., Food, Transport, Bills, Shopping).
- **Account:** The account type (e.g., Credit Card, Debit Card, Cash).
- **Note:** A short note regarding the expense.
- **Description:** A detailed description of the expense entry.

## How to Use

1. **Replace the File Path:**  
   Update the file path in the Python scripts to match your file location. For example, in your script, replace:
   ```python
   FILE_PATH = r'C:/Users/antim/OneDrive/Documents/GitHub/ThinkTrack/budget/expenses/Expense.csv'
   ```
   with:
   ```python
   FILE_PATH = r'Your file location.csv'
   ```

2. **Set Up the Expense CSV File:**  
   Run the header setup script to create the CSV file with the correct header (if it doesn't already exist):
   ```bash
   python expense_header_setup.py
   ```

3. **Add New Expense Entries:**  
   Use the expense tracker script to enter new expense details interactively:
   ```bash
   python expense_tracker.py
   ```

## Template for Adding Expenses

You can use this template format to manually add expenses to the CSV file or enter them using the script:

| Date       | Amount | Category  | Account     | Note          | Description              |
| ---------- | ------ | --------- | ----------- | ------------- | ------------------------ |
| 2025-04-07 | 50.00  | Food      | Credit Card | Lunch at work | Bought lunch at a café   |
| 2025-04-06 | 20.00  | Transport | Cash        | Bus fare      | Travel to the office     |
| 2025-04-05 | 100.00 | Shopping  | Debit Card  | Clothes       | Purchased new T-shirt    |
| 2025-04-04 | 30.00  | Bills     | Online Pay  | Internet Bill | Monthly internet payment |

## Requirements

- Python 3.x is required.
- The scripts use Python's built-in `csv` and `os` modules, so no additional packages are needed.

## Customization

Feel free to modify the scripts to suit your personal requirements. You can change the CSV file path, modify field names, or add additional functionality as needed.

## Happy Tracking!
