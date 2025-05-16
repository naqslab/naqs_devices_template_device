from labscript import Device, config, LabscriptError, set_passed_properties
import numpy as np

class _TemplateChildDevice(Device):
    '''Optional but sometimes necessary backend child device to handle some to
    attached to the parent device (here TemplateDevice) for logical or 
    attribute-based processing.

    Args:
        Device (object): The child device inherits all methods from the Device
        class
    '''
    # def add_device(self, device):
    #     Device.add_device(self, device)
    pass

class TemplateDevice(Device):
    '''Constructs the object that the user will instantiate in both their 
    connection table and experiment script(s).

    Args:
        Device (object): TemplateDevice inherits all methods from the Device
        class.
    '''
    description = 'Template Device, minimal example'
    allowed_children = [_TemplateChildDevice]
    max_instructions = 1e5

    @set_passed_properties(
        property_names = {
            'device_properties' : ['name']
        }
    )

    def __init__(
        self,
        name ='template_device',
        BLACS_connection = 'template_connection',
        **kwargs
    ):
        self.BLACS_connection = BLACS_connection
        Device.__init__(self, name, None, None, **kwargs)

        some_property = 1000

    def generate_code(self, hdf5_file):
        '''Writes instructions to an h5 file to be processed by other 
        labscript components. As an example, we generate 3 columns of random 
        data and use h5py to save the data to the shotfile. Labscript commonly
        makes use of numpy structured arrays to explicitly specify types.

        Args:
            hdf5_file (str): The path to the shot-file, passed in by labscript
            components.
        '''
        group = self.init_device_group(hdf5_file)

        num_instructions = 10
        x_data = np.random.randn(num_instructions)
        y_data = np.random.randn(num_instructions)
        z_data = np.random.randn(num_instructions)

        dtypes = [('x_data', float), ('y_data', float), ('z_data', float)]
        instructions = np.zeros(num_instructions, dtype=dtypes)

        instructions['x_data'] = x_data
        instructions['y_data'] = y_data
        instructions['z_data'] = z_data

        group.create_dataset(
            'programmed_instructions',
            compression=config.compression,
            data=instructions
        )