class Wallet:
    def __init__(self,wallet):
        self._wallet = wallet
        self._balance = 0
        self._transactions = []
    def input_info(self,balance,transactions):
            self._balance = int(balance)
            self._transactions = transactions
    def deposit(self, amount):
        self._balance += amount
        self._transactions.append(f"Deposit:{amount}\n")
    def withdraw(self,amount,address):
        if amount > self._balance:
            return False
        else:
            self._balance -= amount
            self._transactions.append(f"{address}:{amount}")
            return True
    def show_history(self):
        return self._transactions
    def get_info_balance(self):
        return self._balance