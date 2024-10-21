from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from raub import RAUB

class Command:
    
    def __init__(self):
        """Contructor for the command. The robot attribute is for the
        RAUB instance.
        """

        self.robot: RAUB

    def start(self):
        """Runs once at the beginning. 
        """
        
    def execute(self):
        """Runs periodically throughout the command. Should not 
        use with time-dependent functions (unreliable timing?).
        """
        
    def end(self):
        """Runs at the end of the command.
        """
        
    def isFinished(self):
        """Indicates when the command is over. Override and replace. 
        This alternates with execute() in a way. 
        """
        return True
    
    def runCommand(self, robot):
        """Runs the command in the proper sequence. Do not override
        this one. 
        """
        self.robot = robot
        
        self.start()
        while not self.isFinished():
            self.execute()
        self.end()