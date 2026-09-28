def calculate_balance(data):
    """Iterates through data to calculate and display the net balance."""
    print("\n Financial Summary ")
    total_income = 0.0
    total_expense = 0.0

    for record in data:
        if record["type"] == "Income":
            total_income += record["amount"]
        elif record["type"] == "Expense":
            total_expense += record["amount"]

    net_balance = total_income - total_expense

    print(f"Total Income:  {total_income}")
    print(f"Total Expense:  {total_expense}")
    print(" ")
    print(f"Net Balance:  {net_balance}")
