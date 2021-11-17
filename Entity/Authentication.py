

# Imports
from Control.Log_In import Log_In

# This is a public class
class Authentication(Log_In):
    
    # Initializer Method 
    def __init__(self):
        self.password = ""
        self.username = ""
    
    # Getter Method
    def getPassword(self):
        return self.password

    # Setter Method
    def setPassword(self, password):
        self.password = password

    # Getter Method
    def getUser(self):
        return self.username

    # Setter Method
    def setUser(self, username):
        self.username = username

    # Check the user information
    def Check(self, username, password):
        pass


