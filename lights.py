from pymavlink import mavutil

from channels import Channels
from subsystem import Subsystem

class Lights(Subsystem):

    def __init__(self):
        self.channel = Channels.lights1

    def enableLights(self, level=1):
        
        if level > 1 or level < 0:
            raise Exception("Please make sure the brightness level is between 0 and 1.")
            
        self.set_rc_channel_pwm(self.channel, 1100 + level * 800)
    
    def disableLights(self):
        self.set_rc_channel_pwm(self.channel, 1100)
        