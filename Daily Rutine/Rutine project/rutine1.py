import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def add_task_to_google_sheet(date, time, task, category, notes):
    try:
        # Define the scope
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

        # Add credentials
        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)  # Ensure the credentials file is in the same directory
        client = gspread.authorize(creds)

        # Open the Google Sheet
        sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1EScriheq3E8W33obwlpmkEkGvjetWl68sYV9g8U0uFg/edit?gid=0").sheet1

        # Append the data
        sheet.append_row([date, time, task, category, notes])
        print("Task added successfully to Google Sheet!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Add a new task to your Google Sheet daily routine")
    date = input("Enter the date (YYYY-MM-DD): ") or datetime.now().strftime('%Y-%m-%d')
    time = input("Enter the time (e.g., 08:00 AM): ")
    task = input("Enter the task description: ")
    category = input("Enter the category (e.g., Health, Work, Personal, Aim, Study, Exercise): ")
    notes = input("Enter any additional notes: ")

    add_task_to_google_sheet(date, time, task, category, notes)