

# Imports
from Control.Create_Activity import Create_Activity

# This is a public class
class Set_End(Create_Activity):
    
    # Initializer Method 
    def __init__(self):
        self.eventEnd = ""
    
    # Getter Method
    def getEventEnd(self):
        return self.eventEnd

    # Setter Method
    def setEnd(self, end):
        self.eventEnd = end


