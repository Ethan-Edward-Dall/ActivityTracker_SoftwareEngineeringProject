

# Imports

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


