from datetime import date


class Account:
    number = 1000000000
    def __init__(self, owner):
        self.account_number = Account.number
        self.owner = owner
        self.balance  = round(0.00, 2)
        self.created_at = date.today()
        Account.number += 1

    def deposit(self, amount):
        if self.owner.logged_in:
            self.balance += amount
            return f"${amount} deposited successfully"
        return f"User not authenticated"
    
    def check_balance(self):
        if self.owner.logged_in:
            return f"Your account balance is: ${self.balance}"
        return f"User not authenticated"
        

    def transfer(self, amount, reciever_account):
        if self.owner.logged_in:
            if self.balance >= amount:
                reciever_account.balance += amount
                self.balance -= amount
                return f"Transfer of ${amount} was successful!"
        return f"User not authenticated"