import math, time

from pymavlink import mavutil
from pymavlink.quaternion import QuaternionBase
from pymavlink.mavwp import MAVWPLoader

from channels import Channels
from subsystem import Subsystem

class Propellers(Subsystem):
    
    def __init__(self):
        super().__init__()
        
    def setTargetAttitude(roll, pitch, yaw):
        """ Sets the target attitude while in depth-hold mode.

        'roll', 'pitch', and 'yaw' are angles in degrees.
        """
        Subsystem.master.mav.set_attitude_target_send(
            int(1e3 * (time.time() - Subsystem.bootTime)), # ms since boot
            Subsystem.master.target_system, Subsystem.master.target_component,
            # allow throttle to be controlled by depth_hold mode
            mavutil.mavlink.ATTITUDE_TARGET_TYPEMASK_THROTTLE_IGNORE,
            # -> attitude quaternion (w, x, y, z | zero-rotation is 1, 0, 0, 0)
            QuaternionBase([math.radians(angle) for angle in (roll, pitch, yaw)]),
            0, 0, 0, 0 # roll rate, pitch rate, yaw rate, thrust
        )
        
    def setTargetDepth(self, depth):
        """ Sets the target depth while in depth-hold mode. Should
        probably preceed this with a change in operating mode.

        Uses https://mavlink.io/en/messages/common.html#SET_POSITION_TARGET_GLOBAL_INT

        'depth' is technically an altitude, so set as negative meters below the surface
            -> setTargetDepth(-1.5) # sets target to 1.5m below the water surface.
        """
        
        Subsystem.master.mav.set_position_target_global_int_send(
        int(1e3 * (time.time() - Subsystem.bootTime)), # ms since boot
        Subsystem.master.target_system, Subsystem.master.target_component,
        coordinate_frame=mavutil.mavlink.MAV_FRAME_GLOBAL_INT,
        type_mask=( # ignore everything except z position
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_X_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_Y_IGNORE |
            # DON'T mavutil.mavlink.POSITION_TARGET_TYPEMASK_Z_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_VX_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_VY_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_VZ_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_AX_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_AY_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_AZ_IGNORE |
            # DON'T mavutil.mavlink.POSITION_TARGET_TYPEMASK_FORCE_SET |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_YAW_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_YAW_RATE_IGNORE
        ), lat_int=0, lon_int=0, alt=depth, # (x, y WGS84 frame pos - not used), z [m]
        vx=0, vy=0, vz=0, # velocities in NED frame [m/s] (not used)
        afx=0, afy=0, afz=0, yaw=0, yaw_rate=0
        # accelerations in NED frame [N], yaw, yaw_rate
        #  (all not supported yet, ignored in GCS Mavlink)
    )