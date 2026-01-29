class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount must be positive.")
        elif amount > self._balance:
            print("Insufficient balance.")
        else:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")

    def get_balance(self):
        return self._balance


bank=BankAccount("wasil",1000)
bank.deposit(1000)
bank.withdraw(200)
bank.get_balance()