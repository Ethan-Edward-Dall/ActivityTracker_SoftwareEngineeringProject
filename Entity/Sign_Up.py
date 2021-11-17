# Imports
from Control.Log_In import Log_In

# This is a public class
class Sign_Up(Log_In):
    
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

    # Signup Method takes the inputed username and password and add it into the database table
    def signup(self, username, password):
        pass


