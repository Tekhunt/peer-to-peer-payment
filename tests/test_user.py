import pytest
from datetime import date
import hashlib

from user import User

class TestUser:
    def test_register(self):
        user = User()
        assert user.register('user1', 'password1') == 'User successfully registered!'
        assert user.register('user1', 'password2') == 'user with name already exists'
        
    def test_login(self):
        user = User()
        user.register('user1', 'password1')
        user.login('user1', 'password1')
        assert user.logged_in == True
        assert user.login('user1', 'wrong_password') == 'incorrect username or password'
        assert user.login('unknown_user', 'password1') == 'user not found'
        
    def test_logout(self):
        user = User()
        user.register('user1', 'password1')
        user.login('user1', 'password1')
        assert user.logout() == 'You have successfully logged out'
