

# Imports
from Control.Create_Activity import Create_Activity

# This is a public class
class Set_Priority(Create_Activity):
    
    # Initializer Method 
    def __init__(self):
        self.eventPriority = "Neutral"
    
    # Getter Method
    def getPriority(self):
        return self.eventPriority

    # Setter Method
    def setPriority(self, value):
        self.eventPriority = value


