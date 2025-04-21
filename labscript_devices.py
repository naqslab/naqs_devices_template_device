from labscript import Device, config, LabscriptError, set_passed_properties
import numpy as np

class _TemplateChildDevice(Device):
    # def add_device(self, device):
    #     Device.add_device(self, device)
    pass
class TemplateDevice(Device):

    description = 'Template Device, minimal example'
    allowed_children = [_TemplateChildDevice]
    max_instructions = 1e5

    @set_passed_properties(
        property_names = {
            'name',
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
        # self._template_internal_device = _TemplateChildDevice(
        #     name = f'{name}_child_device',
        #     template_child_device = self,
        #     connection = 'internal',
        # )

    # @property
    # def template_internal_device(self):
    #     return self._template_internal_device

    def generate_code(self, hdf5_file):
        group = self.init_device_group(hdf5_file)

        num_instructions = 10
        x_data = np.random.randn(num_instructions)
        y_data = np.random.randn(num_instructions)
        z_data = np.random.randn(num_instructions)

        # Store these instructions to the h5 file:
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