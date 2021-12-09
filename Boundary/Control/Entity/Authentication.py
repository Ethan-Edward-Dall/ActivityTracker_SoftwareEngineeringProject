

# Imports

# This is a public class
class Authentication():

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

    def setErr(self, message):
        self.errLbl.configure(text = message, foreground='red')

    # Check the user information
    def CheckInfo(username, password):
        print("Checking info...")

    # Check the password
    def CheckPass(self, password):
        if(len(password) > 29):
            return False
        return True
