

# Imports
from Control.Create_Activity import Create_Activity

# This is a public class
class Name_Event(Create_Activity):
    
    # Initializer Method 
    def __init__(self):
        self.eventName = ""
    
    # Getter Method
    def getEventName(self):
        return self.eventName

    # Setter Method
    def nameEvent(self, name):
        self.eventName = name


