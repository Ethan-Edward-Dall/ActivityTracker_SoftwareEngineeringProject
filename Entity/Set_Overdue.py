

# Imports
from Control.Complete_Event import Complete_Event

# This is a public class
class Set_Overdue(Complete_Event):
    
    # Initializer Method 
    def __init__(self):
        self.event = ""
    
    # Getter Method
    def getEvent(self):
        return self.event

    # Setter Method
    def setEvent(self, event):
        self.event = event

    # setOverdue Method will take an event from the activity page that due date is before the current time
    def setOverdue(self, event):
        pass


