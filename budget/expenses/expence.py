import csv

# File path
file_path = r'C:/Users/antim/OneDrive/Documents/GitHub/ThinkTrack/budget/expenses/Expense.csv'

# Data to add
data = [
     ["Date", "Amount", "Category", "Account", "Note", "Description"],
     ["2025-04-07", "60","Transport", "Cash", "Taxi", "Home to work"]
]

# Write data to the CSV file
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
     writer = csv.writer(file)
     writer.writerows(data)

print("Data added successfully!")

# Data to add
data1 = [
     ["Date", "Amount", "Category", "Account", "Note", "Description"],
     ["2025-04-07", "60","Transport", "Cash", "bus", "Home to work"]
]

# Write data to the CSV file
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
     writer = csv.writer(file)
     writer.writerows(data1)

print("Data added successfully!")