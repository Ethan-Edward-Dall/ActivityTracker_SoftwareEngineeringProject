

# Imports
from Control.Complete_Event import Complete_Event

# This is a public class
class Manually_Complete(Complete_Event):
    
    # Initializer Method 
    def __init__(self):
        self.event = ""
    
    # Getter Method
    def getEvent(self):
        return self.event

    # Setter Method
    def setEvent(self, event):
        self.event = event

    # end Method will move the activity to completed
    def end(self, event):
        pass

