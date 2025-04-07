import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data(file_path):
    """Load CSV data into a DataFrame."""
    if os.path.exists(file_path):
        return pd.read_csv(file_path, parse_dates=['Date'])
    else:
        print(f"File not found: {file_path}")
        return pd.DataFrame()

def summarize_data(expense_file, income_file):
    """Generate a monthly summary of income and expenses."""
    # Load CSV data
    expenses = load_data(expense_file)
    income = load_data(income_file)
    
    # Ensure the Date column is in datetime format
    expenses['Date'] = pd.to_datetime(expenses['Date'])
    income['Date'] = pd.to_datetime(income['Date'])
    
    # Extract Month-Year for grouping
    expenses['Month'] = expenses['Date'].dt.to_period('M')
    income['Month'] = income['Date'].dt.to_period('M')
    
    # Calculate monthly totals
    expense_summary = expenses.groupby('Month')['Amount'].sum()
    income_summary = income.groupby('Month')['Amount'].sum()
    
    # Combine the summaries into a single DataFrame
    summary = pd.DataFrame({'Income': income_summary, 'Expenses': expense_summary})
    summary['Balance'] = summary['Income'] - summary['Expenses']
    
    return summary

def plot_summary(summary):
    """Generate visualizations for the monthly summary."""
    summary.plot(kind='bar', figsize=(10, 5), title='Monthly Income vs Expenses')
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

def category_pie_chart(expense_file):
    """Generate a pie chart for expense categories."""
    expenses = load_data(expense_file)
    category_summary = expenses.groupby('Category')['Amount'].sum()
    
    plt.figure(figsize=(8, 8))
    category_summary.plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title('Expense Distribution by Category')
    plt.ylabel('')
    plt.show()

def motivation_message(summary):
    """Generate a motivational message based on the balance."""
    last_month = summary.iloc[-1]
    balance = last_month['Balance']
    
    if balance > 0:
        print("Great job! You're saving more than you're spending! Keep it up!")
    elif balance == 0:
        print("You're breaking even. Consider increasing your savings!")
    else:
        print("You're spending more than you're earning. Try budgeting more carefully!")

def main():
    expense_file = r'C:/Users/antim/OneDrive/Documents/GitHub/ThinkTrack/budget/expenses/Expense.csv'
    income_file = r'C:/Users/antim/OneDrive/Documents/GitHub/ThinkTrack/budget/income/Income.csv'
    
    summary = summarize_data(expense_file, income_file)
    print(summary)
    
    plot_summary(summary)
    category_pie_chart(expense_file)
    motivation_message(summary)
    
if __name__ == '__main__':
    main()
