import os
import csv

# Define folder and file paths
data_dir = "data"
users_csv = os.path.join(data_dir, "users.csv")
entries_csv = os.path.join(data_dir, "entries.csv")
recurring_csv = os.path.join(data_dir, "recurring.csv")

# CSV headers
users_header = ["id", "username", "password_hash", "currency"]
entries_header = ["id", "user_id", "type", "amount", "currency", "category", "date", "description"]
recurring_header = ["id", "user_id", "type", "amount", "currency", "category", "frequency", "start_date", "end_date", "last_occurrence"]

def create_csv(file_path, header):
    """
    Creates a CSV file with the specified header if it does not already exist.
    """
    if not os.path.exists(file_path):
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(header)
        print(f"Created file: {file_path}")
    else:
        print(f"File already exists: {file_path}")

def initialize_csv_files():
    """
    Ensures the data folder exists and creates all required CSV files with headers.
    """
    # Create data directory if it doesn't exist
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"Created folder: {data_dir}")

    # Create CSV files with headers
    create_csv(users_csv, users_header)
    create_csv(entries_csv, entries_header)
    create_csv(recurring_csv, recurring_header)

if __name__ == "__main__":
    initialize_csv_files()
