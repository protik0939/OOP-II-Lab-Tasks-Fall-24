"""
Create a custom exception "insufficientFund" if balance is not greater than withdraw amount

     ______________________
     |                    |
     |    BankAccount     |
     |____________________|
     |                    |
     |+ balance           |
     |____________________|
     |                    |
     |+ withdraw(amount)  |---> if amount > balance
     |____________________|            then raise error
                                else print current ammount

"""

class InsufficientFund(Exception):
    def __init__(self, balance, withdraw_amount):
        super().__init__(f"Insufficient funds: Balance {balance}, Withdraw Amount {withdraw_amount}")


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFund(self.balance, amount)
        self.balance -= amount
        print(f"Withdrawal successful. Current balance: {self.balance}")


account = BankAccount(5000)

try:
    account.withdraw(6000)
except InsufficientFund as e:
    print(e)

try:
    account.withdraw(3000)
except InsufficientFund as e:
    print(e)
