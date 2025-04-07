import csv
import os

# File path for transfer CSV file
FILE_PATH = r'C:/Users/antim/OneDrive/Documents/GitHub/ThinkTrack/budget/transfer/Transfer.csv'

def create_header():
    """
    Creates the transfer CSV file with a header if it doesn't exist.
    """
    if os.path.exists(FILE_PATH):
        print("File already exists. Header assumed to be present.")
        return
    
    with open(FILE_PATH, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Date', 'Amount', 'Category', 'Account', 'Note', 'Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        print("Transfer file created and header added successfully.")

if __name__ == '__main__':
    create_header()
# This script creates a CSV file for transfers with a header if it doesn't exist.