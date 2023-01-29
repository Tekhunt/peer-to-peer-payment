import pytest
from datetime import date

from account import Account
from user import User

def test_account_initialization():
    user = User()
    account = Account(user)
    assert account.account_number == 1000000000
    assert account.owner == user
    assert account.balance == 0.00
    assert account.created_at == date.today()

def test_deposit():
    user = User()
    account = Account(user)
    user.register('test', 'password')
    user.login("test", "password")
    deposit_result = account.deposit(100)
    assert deposit_result == "$100 deposited successfully"
    assert account.balance == 100.00

def test_check_balance():
    user = User()
    account = Account(user)
    user.register('test', 'password')
    user.login("test", "password")
    account.deposit(100)
    check_balance_result = account.check_balance()
    assert check_balance_result != "User not authenticated"
    assert "balance" in check_balance_result


def test_transfer():
    user1 = User()
    user1.register('test', 'password')
    user1.login("test", "password")
    user2 = User()
    user1.register('test2', 'password2')
    user2.login("test2", "password2")
    account1 = Account(user1)
    account2 = Account(user2)
    account1.deposit(100)
    transfer_result = account1.transfer(50, account2)
    assert transfer_result == "Transfer of $50 was successful!"
    assert account1.balance == 50.00
    assert account2.balance == 50.00

def test_unauthenticated_user():
    user = User()
    account = Account(user)
    deposit_result = account.deposit(100)
    assert deposit_result == "User not authenticated"
    assert account.balance == 0.00
