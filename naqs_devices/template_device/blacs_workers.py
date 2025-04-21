import time
import labscript_utils.h5_lock
import h5py
from blacs.tab_base_classes import Worker
import labscript_utils.properties as properties

class TemplateDeviceInterface(object):
    """
    This optional class holds the functions / methods for logic processing 
    or commands that go between the device and the front panel. You do not need
    to recompile the connection table if you make changes to this class, only 
    if you change the Worker class below.
    """
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

class TemplateDeviceWorker(Worker):
    """
    Every Worker should generally implement these methods:
    

    `init`: This method initialises communications with the device. 
    Not to be confused with the standard python class __init__ method.
    
    `program_manual`: This method allows for user control of the device via the
    BLACS_tab, setting outputs to the values set in the BLACS_tab widgets.
    
    `check_remote_values`: This method reads the current settings of 
    the device, updating the BLACS_tab widgets to reflect these values.
    
    `transition_to_buffered`: This method transitions the device to buffered 
    shot mode, reading the shot h5 file and taking the saved instructions from 
    labscript_device.generate_code and sending the appropriate commands 
    to the hardware.
    
    `transition_to_manual`: This method transitions the device from buffered 
    to manual mode. It does any necessary configuration to take the device 
    out of buffered mode and is used to read any measurements and save them 
    to the shot h5 file as results.

    """

    def init(self):
        self.intf = TemplateDeviceInterface(self, self.param1, self.param2)
    def program_manual(self, values):
        return {}

    def transition_to_buffered(self, device_name, h5file, initial_values, fresh):
        # get stop time:
        with h5py.File(h5file, 'r') as f:
            props = properties.get(f, self.device_name, 'device_properties')
            # self.stop_time = props.get('stop_time', None) # stop_time may be absent if we are not the master pseudoclock
        return {}
    
    def transition_to_manual(self):
        self.start_time = None
        self.stop_time = None
        return True

    def shutdown(self):
        return

    def abort_buffered(self):
        return self.transition_to_manual()
