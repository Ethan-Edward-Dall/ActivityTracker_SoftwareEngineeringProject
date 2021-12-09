

# Imports

# This is a public class
class Alter_Settings():
    
    # Variables
    

    # alter Settiing values
    def alterSettings():
        pass

# This is a public class
class Toggle_Sound:
    
    # Initializer Method 
    def __init__(self):
        self.volToggle = False
    
    # Getter Method
    def getToggle(self):
        return self.volToggle

    # Setter Method
    def toggleSound(self, toggle):
        self.volToggle = toggle

# This is a public Class
class Adjust_Volume:
    
    # Final Variables
    VOLUME_MAX = 100
    VOLUME_MIN = 1
    
    # Getter Method
    def getVolume(self):
        return self.volLevel

    # Setter Method
    def adjustVolume(self, volume):
        self.volLevel = volume
