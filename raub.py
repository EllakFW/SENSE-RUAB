import time

from pymavlink import mavutil

from subsystem import Subsystem
from lights import Lights
from testcommand import TestCommand
from receiver import Receiver

# Add commands to the list below:
commandSequence = [
    TestCommand()
]

class RAUB:
    
    # Define global subsystems
    lights = Lights()
    receiver = Receiver()

    def __init__(self):
        """ Runs on initiation of the program. Begins
        by setting up the connection to the device. 
        """

        self.master = mavutil.mavlink_connection('udpin:192.168.2.1:14550')
        self.bootTime = time.time()

        self.master.wait_heartbeat()

        # Create subsystems here, and pass them the master. 
        Subsystem.setMaster(self.master, self.bootTime)
                
    def arm(self):
        """Arms the sub.
        """
        self.master.arducopter_arm()

    def disarm(self):
        """Disarms the sub.
        """
        self.master.arducopter_disarm()

    def getData(filter):
        pass
    
from command import Command

# Below is the code that gets ran upon start-up. 
if __name__ == '__main__':
    raub = RAUB()
    receiver = Receiver()
    # Start the thread
    receiver.run()

    # Execute commands sequentially.
    for command in commandSequence:
        try:
            command.runCommand(raub)
        except(BaseException):
            raise Exception(f"-----------------------------------\nERROR WITH COMMAND FROM \
                            {command.__class__}\nRESOLVE BEFORE PROCEEDING\n-----------------------------------")