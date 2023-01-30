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
        positive_amount = (amount*-1) if amount < 0 else amount
        if self.owner.logged_in:
            self.balance += positive_amount
            return f"${positive_amount} deposited successfully"
        return f"User not authenticated"
    
    def check_balance(self):
        if self.owner.logged_in:
            return f"Your account balance is: ${self.balance}"
        return f"User not authenticated"
        

    def transfer(self, amount, reciever_account):
        if not isinstance(reciever_account, Account):
            return "Account does not exist"
        if self.owner.logged_in:
            positive_amount = (amount*-1) if amount < 0 else amount
            if self.balance >= positive_amount:
                reciever_account.balance += positive_amount
                self.balance -= positive_amount
                return f"Transfer of ${positive_amount} was successful!"
        return f"User not authenticated"
    
     
    def withdraw(self, amount):
        positive_amount = (amount*-1) if amount < 0 else amount
        if self.owner.logged_in and positive_amount > 0:
            if self.balance >= positive_amount:
                self.balance -= positive_amount
                return f"Withdraw of ${positive_amount} was successful!"
            else:
                return "Insufficient Balance"