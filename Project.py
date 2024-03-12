import pandas as pd
import numpy as np
from datetime import datetime

# Initialize an empty DataFrame to store expenses
columns = ['Date', 'Category', 'Amount']
expenses_df = pd.DataFrame(columns=columns)

def add_expense(date, category, amount):
    global expenses_df
    expenses_df = expenses_df.append({'Date': date, 'Category': category, 'Amount': amount}, ignore_index=True)
    print(f"Expense of ${amount} added to category '{category}' on {date}.")

def view_expenses():
    global expenses_df
    if expenses_df.empty:
        print("No expenses recorded.")
    else:
        print("Current Expenses:")
        print(expenses_df)

def delete_expense(category, index):
    global expenses_df
    if category not in expenses_df['Category'].unique() or index >= len(expenses_df):
        print("Invalid category or expense index.")
    else:
        deleted_expense = expenses_df[(expenses_df['Category'] == category)].iloc[index]
        expenses_df = expenses_df.drop(index=deleted_expense.name)
        print(f"Expense of ${deleted_expense['Amount']} deleted from category '{category}'.")

# Example usage
add_expense(datetime.now().strftime('%Y-%m-%d'), "Food", 30)
add_expense(datetime.now().strftime('%Y-%m-%d'), "Transportation", 20)
add_expense(datetime.now().strftime('%Y-%m-%d'), "Food", 15)
view_expenses()

print("\nDeleting an expense...")
delete_expense("Food", 0)
view_expenses()
