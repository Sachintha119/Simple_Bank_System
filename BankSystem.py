class BankAccount:
    def __init__(self, account_number, initial_deposit):
        self.account_number = account_number
        self.balance = initial_deposit

    def deposit(self, amount):
        if amount < 0:
            print("Deposit amount must be non-negative.")
            return False
        self.balance += amount
        print(f"${amount} deposited successfully.")
        return True

    def withdraw(self, amount):
        if amount < 0:
            print("Withdrawal amount must be non-negative.")
            return False
        if amount > self.balance:
            print("Insufficient balance.")
            return False
        self.balance -= amount
        print(f"${amount} withdrawn successfully.")
        return True

    def get_balance(self):
        return self.balance


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_deposit):
        if account_number in self.accounts:
            print("Account with this number already exists.")
            return False
        if initial_deposit < 0:
            print("Initial deposit must be non-negative.")
            return False
        new_account = BankAccount(account_number, initial_deposit)
        self.accounts[account_number] = new_account
        print(f"Account {account_number} created with an initial deposit of ${
              initial_deposit}.")
        return True

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            print("Account not found.")
            return False
        return self.accounts[account_number].deposit(amount)

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            print("Account not found.")
            return False
        return self.accounts[account_number].withdraw(amount)

    def check_balance(self, account_number):
        if account_number not in self.accounts:
            print("Account not found.")
            return False
        balance = self.accounts[account_number].get_balance()
        print(f"Account {account_number} balance: ${balance}.")
        return True

    def transfer(self, from_account, to_account, amount):
        if from_account not in self.accounts or to_account not in self.accounts:
            print("One or both accounts not found.")
            return False
        if amount < 0:
            print("Transfer amount must be non-negative.")
            return False
        from_acc = self.accounts[from_account]
        to_acc = self.accounts[to_account]
        if from_acc.withdraw(amount):
            to_acc.deposit(amount)
            print(f"Transferred ${amount} from account {
                  from_account} to account {to_account}.")
            return True
        return False


def main():
    bank_system = BankSystem()

    while True:
        print("\n--- Bank Account Management System ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transfer")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            initial_deposit = float(input("Enter initial deposit: "))
            bank_system.create_account(account_number, initial_deposit)

        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank_system.deposit(account_number, amount)

        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank_system.withdraw(account_number, amount)

        elif choice == "4":
            account_number = input("Enter account number: ")
            bank_system.check_balance(account_number)

        elif choice == "5":
            from_account = input("Enter source account number: ")
            to_account = input("Enter destination account number: ")
            amount = float(input("Enter transfer amount: "))
            bank_system.transfer(from_account, to_account, amount)

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

