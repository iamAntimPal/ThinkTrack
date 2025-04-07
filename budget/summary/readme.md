# Monthly Summary Tracker

This project helps track your monthly income and expenses, providing insights through visual charts and summary data. The script reads financial data from CSV files, calculates monthly totals, and generates helpful visualizations.

## Features
- **Monthly Summary Calculation**: Computes income, expenses, and net balance.
- **Bar Chart Visualization**: Displays a monthly comparison of income vs. expenses.
- **Category Pie Chart**: Shows the distribution of expenses by category.
- **Motivational Message**: Provides feedback based on spending and saving trends.

## File Structure
- `monthly_summary.py` – The main script to generate financial summaries and charts.
- `expense.csv` – Stores expense data.
- `income.csv` – Stores income data.

## CSV File Format
The CSV files should have the following columns:
```
Date, Amount, Category, Account, Note, Description
```
- **Date**: YYYY-MM-DD format.
- **Amount**: Numeric value of income or expense.
- **Category**: Expense or income category (e.g., Food, Salary).
- **Account**: Payment method (e.g., Cash, Credit Card, Bank Transfer).
- **Note**: Short description.
- **Description**: Detailed transaction notes.

## How to Use
### 1. Install Dependencies
Ensure you have Python 3.x installed along with required libraries:
```bash
pip install pandas matplotlib
```

### 2. Update File Paths
Modify `expense_file` and `income_file` paths in `monthly_summary.py`:
```python
expense_file = r'path_to/Expense.csv'
income_file = r'path_to/Income.csv'
```

### 3. Run the Script
Execute the script to generate charts and summaries:
```bash
python monthly_summary.py
```

## Example Output
### Summary Table
```
        Income  Expenses  Balance
2025-03  5000.0   3000.0   2000.0
2025-04  5500.0   3200.0   2300.0
```

### Visualizations
- **Bar Chart:** Monthly comparison of income vs. expenses.
- **Pie Chart:** Distribution of expenses by category.

## Motivation
Tracking your income and expenses helps in financial planning and ensures better budgeting. Use this script to maintain financial discipline and improve savings!

---
Happy tracking! 🚀