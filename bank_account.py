from random import randint
from datetime import datetime


class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        with open(f"{self.account_number}.txt", "a") as file:
            file.write(f"Deposited: {amount}, {datetime.now()}\n")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
            return
        with open(f"{self.account_number}.txt", "a") as file:
            file.write(f"withdraw: {amount}, {datetime.now()}\n")
        self.balance -= amount

    def get_balance(self):
        return f"Account Balance: {self.balance}"

    def display_transaction_history(self):
        with open(f"{self.account_number}.txt", "r") as file:
            print(file.read())


if __name__ == "__main__":
    print("Welcome to Bank Account Management System\n")
    print("1. Create Account")
    print("2. Use an existing account")
    print("3. Exit")
    selected_option = int(input("Enter your option: "))

    if selected_option == 1:
        account_holder = input("Enter your name: ")
        account_number = randint(100000, 999999)
        created = False
        with open("accounts.txt", "r") as file:
            lines = file.readlines()
            while (not created):
                created = True
                for line in lines:
                    if str(account_number) in line:
                        created = False
                        account_number = randint(100000, 999999)
                        break

        if (created):
            account = BankAccount(account_holder, account_number)
            with open("accounts.txt", "a") as file:
                file.write(f"{account_number}, {account_holder}, 0\n")
            print(
                f"Account created successfully with account number: {account.account_number}")
        else:
            print("Account number already exists")

        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Transaction History")
            print("5. Exit")
            selected_option = int(input("Enter your option: "))
            if selected_option == 1:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif selected_option == 2:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif selected_option == 3:
                print(account.get_balance())
            elif selected_option == 4:
                account.display_transaction_history()
            elif selected_option == 5:
                with open("accounts.txt", "r+") as file:
                    lines = file.readlines()
                    for index, line in enumerate(lines):
                        if str(account_number) in line:
                            lines[index] = f"{account_number}, {account_holder}, {account.balance}\n"
                            break

                    file.seek(0)
                    file.writelines(lines)
                    file.truncate()
                break
            else:
                print("Invalid Option")

    if selected_option == 2:
        account_number = int(input("Enter your account number: "))
        account_info = None
        account_exists = False
        with open("accounts.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if str(account_number) in line:
                    account_exists = True
                    account_info = line.split(", ")
                    break

        if account_exists:
            account = BankAccount(
                account_info[1], account_info[0], float(account_info[2]))
            print("Account found successfully")
        else:
            print("Account not found")
            exit()

        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Transaction History")
            print("5. Exit")
            selected_option = int(input("Enter your option: "))
            if selected_option == 1:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif selected_option == 2:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif selected_option == 3:
                print(account.get_balance())
            elif selected_option == 4:
                account.display_transaction_history()
            elif selected_option == 5:
                with open("accounts.txt", "r+") as file:
                    lines = file.readlines()
                    for index, line in enumerate(lines):
                        if str(account_number) in line:
                            lines[index] = f"{account.account_number}, {account.account_holder}, {account.balance}\n"
                            break

                    file.seek(0)
                    file.writelines(lines)
                    file.truncate()
                break
            else:
                print("Invalid Option")

    if selected_option == 3:
        exit()
