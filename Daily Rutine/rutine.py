import csv
from datetime import datetime

def add_task_to_csv(date, time, task, category, notes):
    file_path = 'rutine.csv'
    
    # Open the CSV file in append mode
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, time, task, category, notes])

if __name__ == "__main__":
    print("Add a new task to your daily routine")
    date = input("Enter the date (YYYY-MM-DD): ") or datetime.now().strftime('%Y-%m-%d')
    time = input("Enter the time (e.g., 08:00 AM): ")
    task = input("Enter the task description: ")
    category = input("Enter the category (e.g., Health, Work, Personal): ")
    notes = input("Enter any additional notes: ")

    add_task_to_csv(date, time, task, category, notes)
    print("Task added successfully!")