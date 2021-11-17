

# Imports
from Control.Alter_Settings import Alter_Settings

# This is a public class
class Toggle_Sound(Alter_Settings):
    
    # Initializer Method 
    def __init__(self):
        self.volToggle = False
    
    # Getter Method
    def getToggle(self):
        return self.volToggle

    # Setter Method
    def toggleSound(self, toggle):
        self.volToggle = toggle


