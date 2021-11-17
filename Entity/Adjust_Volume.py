

# Imports
from Control.Alter_Settings import Alter_Settings

# This is a public Class
class Adjust_Volume(Alter_Settings):
    
    # Final Variables
    VOLUME_MAX = 100
    VOLUME_MIN = 1

    # Initializer Method 
    def __init__(self):
        self.volLevel = 50
    
    # Getter Method
    def getVolume(self):
        return self.volLevel

    # Setter Method
    def adjustVolume(self, volume):
        self.volLevel = volume


