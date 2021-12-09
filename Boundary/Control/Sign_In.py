

# Imports

# This is a public class
class Sign_In():

    # Calcualte input
    def login(username, password):
        if(Authentication.CheckPass(password) and Authentication.CheckInfo(username, password)):
            return True
        else:
            return False

    def returnUser():
        return Sign_Up.getUser()

    def returnPass():
        return Sign_Up.getPassword()

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

    # Check the user information
    def CheckInfo(username, password):
        print("Checking info...")
        return True

    # Check the password
    def CheckPass(password):
        if(len(password) > 29):
            return False
        return True

# This is a public class
class Sign_Up():
    
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