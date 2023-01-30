import hashlib

class User:
    def __init__(self):
        self.users = {}
        self.logged_in = False

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password):
        password = str(password)
        if username in self.users.values():
            return f'user with name already exists'
        else:
            self.users['username'] = username
            self.users['password'] = self.hash_password(password)
            return 'User successfully registered!'
    
    def login(self, username, password):
        password = str(password)
        if username in self.users.values():
            if (username == self.users.get('username')) & (self.hash_password(password) == self.users.get('password')):
                self.logged_in = True
            else:
                return 'incorrect username or password'
        else:
            return 'user not found'
    def logout(self):
        self.logged_in = False
        return 'You have successfully logged out'