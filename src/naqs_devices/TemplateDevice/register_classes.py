
from labscript_devices import register_classes

register_classes(
    labscript_device_name='TemplateDevice',
    BLACS_tab='naqs_devices.TemplateDevice.blacs_tabs.TemplateDeviceTab',
    runviewer_parser='naqs_devices.TemplateDevice.runviewer_parser.TemplateDeviceParser',
)
