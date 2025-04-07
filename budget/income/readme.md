
# Income Tracker

This repository contains Python scripts to manage and record your income data using CSV files. The scripts allow you to create the CSV file with a header, add an initial income record, and append new income entries interactively.

## File Structure

- **Income Header Setup:**  
  `income_header_setup.py`  
  This script creates the income CSV file with the following header if it doesn't exist:
  ```
  Date,Amount,Category,Account,Note,Description
  ```


- **Income Tracker:**  
  `income_tracker.py`  
  This script lets you add new income entries via the command line. It appends your data to the CSV file without overwriting any existing content.

- **income.csv:**
  `income.csv`
  This is the file that all income data stored. 

## CSV File Format

The CSV file is structured with the following headers:
- **Date:** The date of the income entry (format: YYYY-MM-DD).
- **Amount:** The amount received.
- **Category:** The income category (e.g., Salary, Freelance, Interest).
- **Account:** The account type (e.g., Bank Transfer, Cash).
- **Note:** A short note regarding the income.
- **Description:** A detailed description of the income entry.

## How to Use

1. **Replace the File path to your File Location and give your file path for working**
   - Run the command for that:
     ```python
     # File path for income CSV file
     FILE_PATH = r'C:/Users/antim/OneDrive/Documents/GitHub/ThinkTrack/budget/income/Income.csv'
     #replace with
     FILE_PATH = r'Your file location.csv'
      ```  

2. **Set Up the Income CSV File:**
   - Run the header setup script to create the CSV file with the correct header (if it doesn't already exist):
     ```bash
     python income_header_setup.py
     ```

3. **Add New Income Entries:**
   - Use the income tracker script to enter new income details interactively:
     ```bash
     python income_tracker.py
     ```

## Requirements

- Python 3.x is required.
- The scripts use Python's built-in `csv` and `os` modules, so no additional packages are needed.

## Customization

Feel free to modify the scripts to suit your personal requirements. You can change the CSV file path, modify field names, or add additional functionality as needed.

## Happy tracking!
