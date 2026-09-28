from storage import save_data

def add_transaction(data):
    """Handles user input to create a new income or expense record."""
    print("\n Add Transaction- ")
    t_type = input("Is this Income or Expense? (Enter I or E): ").strip().upper()

    if t_type not in ['I', 'E']:
        print("Error: Invalid input. Please enter I or E.")
        return

    try:
        # prevents crash if user types text instead of numbers
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Error: Amount must be greater than 0.")
            return
    except ValueError:
        print("Error: Please enter a valid numerical amount.")
        return

    desc = input("Enter a short description (e.g. street food, pocket money etc): ").strip()

    # Create a dictionary for the transaction
    record = {
        "type": "Income" if t_type == 'I' else "Expense",
        "amount": amount,
        "description": desc
    }

    data.append(record)
    save_data(data) # Automatically triggers save for reliability
    print("Transaction added securely!")

def view_transactions(data):
    """Displays all saved transactions in a list."""
    print("\n All Transactions ")
    if not data:
        print("No transactions found. Please add some first.")
        return

    for index, record in enumerate(data, start=1):
        print(f"{index}. {record['type']} | Amount: {record['amount']} | Description: {record['description']}")

