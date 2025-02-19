import pandas as pd

class ExpenseTracker:
    def __init__(self):
        
        self.expenses = pd.DataFrame(columns=["Date", "Category", "Amount"])
    def add_expense(self, date, category, amount):
        """Add an expense to the tracker."""
        new_expense = {"Date": date, "Category": category, "Amount": amount}
        self.expenses = pd.concat([self.expenses, pd.DataFrame([new_expense])], ignore_index=True)
        print(f"Added: {new_expense}")
    def view_expenses(self):
        """View all expenses."""
        if self.expenses.empty:
            print("No expenses to show.")
        else:
            print("Expenses:")
            print(self.expenses)
    def visualize_expenses(self):
        """Visualize expenses by category."""
        if self.expenses.empty:
            print("No expenses to visualize.")
            return
        
        category_totals = self.expenses.groupby("Category")["Amount"].sum()
        
def main():
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add an expense")
        print("2. View expenses")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category (e.g., Food, Travel, Bills): ")
            amount = float(input("Enter the amount: "))
            tracker.add_expense(date, category, amount)
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "4":
            print("Exiting Expense Tracker. Thankyou for using!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
