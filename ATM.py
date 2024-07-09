class ATM:
    def __init__(self):
        self.balance = 0.0
        self.pin = "1234"  # Default PIN

    def check_balance(self, pin):
        if self.validate_pin(pin):
            print(f"Your current balance is: ${self.balance:.2f}")
        else:
            print("Invalid PIN")

    def deposit(self, amount, pin):
        if self.validate_pin(pin):
            if amount > 0:
                self.balance += amount
                print(f"Successfully deposited ${amount:.2f}")
            else:
                print("Deposit amount must be positive")
        else:
            print("Invalid PIN")

    def withdraw(self, amount, pin):
        if self.validate_pin(pin):
            if amount > 0:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Successfully withdrew ${amount:.2f}")
                else:
                    print("Withdrawal amount invalid")
            else:
                print("Withdrawal amount must be positive")
        else:
            print("Invalid PIN")

    def validate_pin(self, pin):
        return pin == self.pin

atm = ATM()

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        pin = input("Enter your PIN: ")
        atm.check_balance(pin)
    elif choice == '2':
        pin = input("Enter your PIN: ")
        try:
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount, pin)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == '3':
        pin = input("Enter your PIN: ")
        try:
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount, pin)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid option, please choose a valid option")
