import os

class Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for account in self.accounts.values():
                f.write(f"Account Number: {account.account_number}, Account Holder: {account.account_holder}, Balance: {account.balance}\n")

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                account_number, account_holder, balance = line.split("Account Number: ")[1].split(',')[0].strip(), line.split("Account Holder: ")[1].split(',')[0].strip(), line.split("Balance: ")[1].strip()
                account = Account(int(account_number), account_holder, int(balance))
                self.add_account(account)

    def perform_operation(self):
        while True:
            print("\n1. Add account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("9. Save and Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                account_number = int(input("Enter account number: "))
                account_holder = input("Enter account holder name: ")
                balance = int(input("Enter initial balance: "))
                account = Account(account_number, account_holder, balance)
                self.add_account(account)

            elif choice == 2:
                account_number = int(input("Enter account number: "))
                amount = int(input("Enter amount: "))
                if account_number in self.accounts:
                    self.accounts[account_number].deposit(amount)
                    print("Deposit Successful")
                else:
                    print("Account not found")

            elif choice == 3:
                account_number = int(input("Enter account number: "))
                amount = int(input("Enter amount: "))
                if account_number in self.accounts:
                    self.accounts[account_number].withdraw(amount)
                    print("Withdrawal Successful")
                else:
                    print("Account not found")

            elif choice == 4:
                account_number = int(input("Enter account number: "))
                if account_number in self.accounts:
                    print("Current Balance: ", self.accounts[account_number].get_balance())
                else:
                    print("Account not found")

            elif choice == 9:
                filename = input("Enter filename to save data: ")
                self.save_to_file(filename)
                print("Data saved successfully")
                break
