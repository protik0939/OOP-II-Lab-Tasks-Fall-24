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