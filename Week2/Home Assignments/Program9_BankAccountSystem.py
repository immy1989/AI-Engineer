class BankAccount:
    def __init__(self, account_holder, balance, account_type):
        # Initialize attributes
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type
    
    def deposit(self, amount):
        # Deposit money into the account
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        # Withdraw money from the account if sufficient balance exists
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Type: {self.account_type}")
        # Display the current balance
        print(f"Current balance is {self.balance}.")

if __name__ == "__main__":
    # Create a bank account instance and demonstrate functionality
    account1 = BankAccount("John Doe", 1000, "Savings")
    account2 = BankAccount("Jane Smith", 2000, "Current")
    
    print("=== Initial Account Details ===")
    account1.display_balance()
    print("\n=== Depositing Money ===")
    account1.deposit(500)
    print("\n=== Withdrawing Money ===")
    account1.withdraw(300)    
    print("\n=== Final Account Details ===")
    account1.display_balance()

    print("=== Initia Account Details ===")
    account2.display_balance()
    print("\n=== Depositing Money ===")
    account2.deposit(1000)      
    print("\n=== Withdrawing Money ===")
    account2.withdraw(5000)      # Attempt to withdraw more than the balance
    account2.withdraw(1500)      # Valid withdrawal
    print("\n=== Final Account Details ===")
    account2.display_balance()

