

# Imports
from Control.Create_Activity import Create_Activity

# This is a public class
class Set_Note(Create_Activity):

    # Initializer Method 
    def __init__(self):
        self.note = ""
    
    # Getter Method
    def readNote(self):
        return self.note

    # Setter Method
    def addNote(self, note):
        self.note = note

