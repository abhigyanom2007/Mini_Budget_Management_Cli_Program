from storage import load_data
from transactions import add_transaction, view_transactions
from analytics import calculate_balance

def main():
    """Main loop for the CLI application menu."""
    print("Welcome to your Mini Budget CLI program")
    # Load any existing data when the app starts
    data = load_data()

    while True:
        print("\n Main Menu ")
        print("1. Add a Transaction")
        print("2. View All Transactions")
        print("3. Check Balance")
        print("4. Exit App")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_transaction(data)
        elif choice == '2':
            view_transactions(data)
        elif choice == '3':
            calculate_balance(data)
        elif choice == '4':
            print("Exiting app.... Your data is safely stored. see ya!")
            break
        else:
            print("Invalid choice, Please type a number from 1 to 4.")

if __name__ == "__main__":
    # Ensures this script runs only when executed directly from the command line
    main()