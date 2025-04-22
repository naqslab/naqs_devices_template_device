import numpy as np

from naqs_devices.Helpers import ScopeChannel
from labscript import Device, TriggerableDevice, config, LabscriptError, set_passed_properties

__version__ = '0.1.0'
__author__ = ['dihm']      
                      
class TemplateDevice(Device):
    description = '''
    Template Device for Labscript, can be repurposed to make your own device
    '''
    allowed_children = [ScopeChannel]
    
    @set_passed_properties(property_names = {
        'device_properties':['name',]}
        )
    def __init__(self, name='TemplateDevice', **kwargs):

        self.name = name
        self.BLACS_connection = 'template_connection'
        
    def generate_code(self, hdf5_file):
        
        num_instructions = 10
        x_data = np.random.randn(num_instructions)
        y_data = np.random.randn(num_instructions)
        z_data = np.random.randn(num_instructions)

        dtypes = np.dtype(('x_data', float),
                          ('y_data', float),
                          ('z_data', float))
        
        out_table = np.zeros(num_instructions, dtype=dtypes)

        out_table['x_data'] = x_data
        out_table['y_data'] = y_data
        out_table['z_data'] = z_data


        group = self.init_device_group(hdf5_file)
        group.create_dataset('SOME_DATA', data=out_table)
