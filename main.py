
from account import Account
from user import User

user1 = User()
account = Account(user1)
user1.register('user1', '1234')
user1.login('user1', '1234')
user2 = User()
account = Account(user2)
user2.register('user2', '1234')
user2.login('user2', '1234')
account1 = Account(user1)
account2 = Account(user2)
print(account1.__dict__)
print(account2.__dict__)
print(user1.users)
print(user2.users)
account1.deposit(10)
account2.deposit(20)
account2.transfer(15, account1)
print(account1.check_balance())
print(account2.check_balance())
print(account1.transfer(25, account2))
print(account1.check_balance())
print(account2.check_balance())
print(account2.withdraw(-20))
print(account2.check_balance())
print(account1.withdraw(-20))
# Should print insufficient balance


