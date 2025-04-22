#####################################################################
#                                                                   #
# /naqs_devices_template_device/__init__.py                         #
#                                                                   #
# Copyright 2025, Jason Pruitt                                      #
#                                                                   #
# This file is part of the naqslab devices extension to the         #
# labscript_suite. It is licensed under the Simplified BSD License. #
#                                                                   #
#                                                                   #
#####################################################################

# basic init for naqs_devices_template_device
# defines a version and author    
import labscript_devices

__version__ = '0.1.0'
__author__ = ['Json-To-String']

##############################################
# define helper sub-classes of labscript defined channels

from labscript import Device, AnalogIn, StaticDDS, LabscriptError

class HelperClass():
    pass