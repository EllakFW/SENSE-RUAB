class Subsystem:
    """
    Used for universal subsystems. All of them
    should inherit this class. Things shared across
    all of them are defined here.
    """
    master = None
    bootTime = None

    @staticmethod
    def setMaster(master_, bootTime_):
        """ Sets the master of all of the
        subsystems. Also sets the boot time.
        """
        Subsystem.master = master_ # Test to make sure this object is the same for all subsystems
        Subsystem.bootTime = bootTime_ 

    def set_rc_channel_pwm(self, channel_id, pwm=1500):
        """ Set RC channel pwm value
        Args:
            channel_id : Channel ID (1-18)
            pwm : Channel pwm value (1100-1900)
        """ 
        if channel_id < 1 or channel_id > 18:
            print("Channel does not exist.")
            return

        # Mavlink 2 supports up to 18 channels:
        # https://mavlink.io/en/messages/common.html#RC_CHANNELS_OVERRIDE
        rc_channel_values = [65535 for _ in range(18)]
        rc_channel_values[channel_id - 1] = pwm
        self.master.mav.rc_channels_override_send(
            self.master.target_system,                  # target_system
            self.master.target_component,               # target_component
            *rc_channel_values)                         # RC channel list, in microseconds.    
