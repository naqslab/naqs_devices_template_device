
from labscript_devices import register_classes

'''
This file sets up your device within the import machinery of labscript (via
the `register_classes` function). Labscript will first look within 
labscript-devices, but will then compare against the variables you set here. Be
sure that you also specify your namespace in `user_devices` under the [DEFAULT]
section in the `your_apparatus.ini` file.
'''

register_classes(
    labscript_device_name='TemplateDevice',
    BLACS_tab='naqs_devices.TemplateDevice.blacs_tabs.TemplateDeviceTab',
    runviewer_parser='naqs_devices.TemplateDevice.runviewer_parsers.TemplateDeviceParser',
)
