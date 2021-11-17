

# Imports
from Control.Create_Activity import Create_Activity

# This is a public class
class Set_Start(Create_Activity):
    
    # Initializer Method 
    def __init__(self):
        self.eventStart = ""
    
    # Getter Method
    def getEventStart(self):
        return self.eventStart

    # Setter Method
    def setStart(self, start):
        self.eventStart = start


