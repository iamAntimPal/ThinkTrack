import csv
import os

# File path for income CSV file
FILE_PATH = r'C:/Users/antim/OneDrive/Documents/GitHub/ThinkTrack/budget/income/income.csv'

def create_header():
    """
    Creates the income CSV file with a header if it doesn't exist.
    """
    if os.path.exists(FILE_PATH):
        print("File already exists. Header assumed to be present.")
        return
    
    with open(FILE_PATH, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Date', 'Amount', 'Category', 'Account', 'Note', 'Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        print("File created and header added successfully.")

if __name__ == '__main__':
    create_header()
