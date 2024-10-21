from command import Command

import time

class TestCommand(Command):
    def __init__(self):
        super().__init__()
    
    def start(self):
        self.robot.lights.enableLights()
                        
        time.sleep(5)
        
        self.robot.lights.disableLights()