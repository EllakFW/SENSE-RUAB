"""
Use a dictionary to store messages

{"a" : 1, "b" : 2}

in this case the "a" would be like "attitude". The 1 would be the most recent attitutde message. 

Constantly check for messages and update the dictionary in a thread function.

Ex: 

x = threading.Thread(target=thread_function, args=(1,))
x.start()

https://realpython.com/intro-to-python-threading/#starting-a-thread

https://stackoverflow.com/questions/15365406/run-class-methods-in-threads-python



"""

""""
In raub
import Reciver
input.run()
"""
import threading
import time
from subsystem import Subsystem

class Receiver(Subsystem):

    def __init__(self):
        self.msg_recent = {
            "SYS_STATUS": "", 
            "POWER_STATUS" : "",
            "SCALED_IMU2": "",
            "MEMINFO" : "",
            "NAV_CONTROLLER_OUTPUT": "",
            "MISSION_CURRENT" : "",
            "SERVO_OUTPUT_RAW": "",
            "RC_CHANNELS" : "",
            "RAW_IMU": "",
            "chan6_raw" : "",
            "SCALED_PRESSURE": "",
            "chan14_raw" : "",
            "SCALED_PRESSURE2": "",
            "GPS_RAW_INT" : "",
            "NAMED_VALUE_FLOAT": "",
            "ATTITUDE" : "",
            "VFR_HUD" : "",
            "AHRS2" : "",
            "GLOBAL_POSITION_INT" : "",
            "SYSTEM_TIME" : "",
            "AHRS" : "",
            "HWSTATUS" : "",
            "RANGEFINDER" : "",
            "MOUNT_STATUS" : "",
            "EKF_STATUS_REPORT" : "",
            "VIBRATION" : "",
            "BATTERY_STATUS" : "",
        }
    
    def thread_function(self):
        i = 0
        while i<100:
            msg = self.master.recv_match()

            print(msg)
            i = i+1
            if msg != None :
                print(msg.get_type())
                self.msg_recent[msg.get_type()] = msg
                print(self.msg_recent[msg.get_type()])
                pass
           
    def run(self):
        x = threading.Thread(target=self.thread_function,)
        x.start()

    def getValue(self, valueToReturn):
        return self.msg_recent(valueToReturn)
        

        