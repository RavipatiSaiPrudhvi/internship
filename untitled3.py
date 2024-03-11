class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category].append(amount)
        else:
            self.expenses[category] = [amount]

    def view_expenses(self):
        for category, amounts in self.expenses.items():
            total = sum(amounts)
            print(f"{category}: {total}")

    def total_expenses(self):
        total = 0
        for amounts in self.expenses.values():
            total += sum(amounts)
        return total


def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            tracker.add_expense(category, amount)
            print("Expense added successfully!")
        elif choice == "2":
            print("\nExpenses:")
            tracker.view_expenses()
        elif choice == "3":
            total = tracker.total_expenses()
            print(f"Total Expenses: {total}")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
