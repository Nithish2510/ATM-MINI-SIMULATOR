import random

def atm_simulation():
    print("========================================")
    print("        MARIYAMMAN INDIAN BANK ATM      ")
    print("========================================")

    # 1. Login: Accepts ANY non-empty account number and PIN/password
    while True:
        account_number = input("\nEnter Account Number: ").strip()
        password = input("Enter  PIN / Password: ").strip()

        if account_number != "" and password != "":
            break
        else:
            print("Error: Account Number and Password cannot be blank. Please try again.")

    # 2. Generate Random Account Holder Name and Random Balance
    names = [
        "Arun Kumar", "Priya Sharma", "Karthik Raja", "Divya Nair", 
        "Rahul Verma", "Sneha Patel", "Vikram Singh", "Ananya Rao"
    ]
    account_holder = random.choice(names)
    
    # Generates a random balance between Rs. 1,000 and Rs. 50,000 (rounded to 2 decimal places)
    balance = round(random.uniform(1000, 50000), 2)

    print("\n----------------------------------------")
    print("Login Successful!")
    print(f"Account Holder : {account_holder}")
    print(f"Account Number : {account_number}")
    print(f"Current Balance: Rs. {balance:.2f}")
    print("----------------------------------------")

    history = [f"Opening Balance: Rs. {balance:.2f}"]

    # 3. Main ATM Menu Loop
    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Mini Statement")
        print("5. Change PIN / Password")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            print(f"\nAccount Holder : {account_holder}")
            print(f"Current Balance: Rs. {balance:.2f}")

        elif choice == "2":
            amount_str = input("\nEnter amount to deposit: Rs. ").strip()
            try:
                amount = float(amount_str)
                if amount > 0:
                    balance += amount
                    history.append(f"Deposited : +Rs. {amount:.2f} | Balance: Rs. {balance:.2f}")
                    print(f"Successfully deposited Rs. {amount:.2f}")
                    print(f"Updated Balance: Rs. {balance:.2f}")
                else:
                    print("Error: Deposit amount must be greater than 0.")
            except ValueError:
                print("Error: Invalid input. Please enter numbers only.")

        elif choice == "3":
            amount_str = input("\nEnter amount to withdraw: Rs. ").strip()
            try:
                amount = float(amount_str)
                if amount <= 0:
                    print("Error: Withdrawal amount must be greater than 0.")
                elif amount > balance:
                    print(f"Error: Insufficient balance! Your balance is Rs. {balance:.2f}")
                else:
                    balance -= amount
                    history.append(f"Withdrew  : -Rs. {amount:.2f} | Balance: Rs. {balance:.2f}")
                    print(f"Please collect your cash: Rs. {amount:.2f}")
                    print(f"Remaining Balance: Rs. {balance:.2f}")
            except ValueError:
                print("Error: Invalid input. Please enter numbers only.")

        elif choice == "4":
            print("\n=========== MINI STATEMENT ===========")
            print(f"Account Holder : {account_holder}")
            print(f"Account Number : {account_number}")
            print("-" * 38)
            for item in history:
                print(item)
            print("-" * 38)
            print(f"Available Bal  : Rs. {balance:.2f}")
            print("======================================")

        elif choice == "5":
            new_pin = input("\nEnter new PIN / Password: ").strip()
            if new_pin != "":
                password = new_pin
                print("PIN / Password updated successfully!")
            else:
                print("Error: PIN cannot be empty.")

        elif choice == "6":
            print(f"\nThank you for banking with us, {account_holder}! Goodbye.")
            break

        else:
            print("\nInvalid choice! Please enter a number from 1 to 6.")


# Run the program
if __name__ == "__main__":
    atm_simulation()
