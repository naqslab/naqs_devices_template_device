import labscript_utils.h5_lock
import h5py
import numpy as np

class TemplateDeviceParser(object):

    def __init__(self, path, device):
        self.path = path
        self.name = device.name
        self.device = device
