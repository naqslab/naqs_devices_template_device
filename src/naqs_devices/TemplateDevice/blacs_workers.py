import time
import labscript_utils.h5_lock
import h5py
from blacs.tab_base_classes import Worker
import labscript_utils.properties as properties

class TemplateDeviceInterface(object):
    '''
    This optional class holds the functions / methods for logic processing 
    or commands that go between the device hardware and the front panel. It is
    automatically called by BLACS.
    '''
    # def __init__(self, param1, param2):
    #     self.param1 = param1
    #     self.param2 = param2
    def __init__(self):
        pass

class TemplateDeviceWorker(Worker):
    '''Handles processing of data between a shot's h5file and the Device.
    Every Device's Worker should generally implement the methods defined in 
    this TemplateDeviceWorker.

    Args:
        Worker (Process):  Inherited from `blacs.tab_base_classes.py`.
    '''

    def init(self):
        '''Initialises communications with the device. Not to be confused with
        the standard python class __init__ method.
        '''
        
        # self.intf = TemplateDeviceInterface(self, self.param1, self.param2)
        self.intf = TemplateDeviceInterface()

    def program_manual(self, values):
        '''Allows for user control of the device via the BLACS_tab, setting 
        outputs to the values set in the BLACS_tab widgets.

        Args:
            values (dict): dictionary of values to update front panel.

        Returns:
            dict: returns are of dictionary shape to allow use from other
            methods.
        '''
        # some logic here to update your device's front panel
        self.logger.info('\nUpdating front panel...')
        self.logger.info(values)
        return values
    
    def check_remote_values(self):
        '''Queries and reads current settings of the device, updating the
        BLACS_tab widgets to reflect these values.

        Returns:
            dict: returns an empty dictionary, can be populated depending on 
            level of device feedback.
        '''
        self.logger.info('\nChecking remote values...')

        results = {}
        # Do some logic to populate the results dict depending on your device
        return results

    def transition_to_buffered(
            self,
            device_name : str,
            h5file : str,
            initial_values : dict,
            fresh
            ):
        '''This method transitions the device from buffered to manual mode. It 
        does any necessary configuration to take the device out of buffered
        mode and is used to read any measurements and save them to the shot h5
        file as results.

        Args:
            device_name (str): Name of the device in labscript.
            h5file (str): path to shot file to run.
            initial_values (dict): Dictionary of output states at shot start
            fresh (bool): 

        Returns:
            dict: Dictionary of expected final output states.
        '''

        # Store the initial values in case we have to abort and restore them:
        self.initial_values = initial_values
        # Store the final values for use during transition_to_manual:
        self.final_values = initial_values

        # get stop time:
        with h5py.File(h5file, 'r') as f:
            props = properties.get(f, self.device_name, 'device_properties')
            # self.stop_time = props.get('stop_time', None) # stop_time may be absent if we are not the master pseudoclock
        return self.final_values
    
    def transition_to_manual(self):
        '''Logic that runs after buffered execution to return control to the 
        user/front panel. May need to call :meth:`abort_buffered` to handle 
        behavior such as timeouts.

        Returns:
            Bool: returns True for internal logic.
        '''
        self.start_time = None
        self.stop_time = None
        return True

    def shutdown(self):
        '''Ends communication with the device. Often calls upon a close method.
        '''
        return
    
    def abort_transition_to_buffered(self):
        return self.transition_to_manual()
    
    def abort_buffered(self):
        '''Called when the user presses the abort button during buffered
        execution. Here returns to initial values, since buffered execution 
        needed to be stopped.
        '''

        self.program_manual(self.initial_values)

        return True
