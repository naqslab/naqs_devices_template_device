Installation
============

Prerequiste: labscript_devices >= 2.6.0

Clone this repository into the labscript_suite directory. Typically into
:file:`userlib` or the main directory level.

Next, modify your labconfig.ini file to recognize the module by adding the following entry to the :file:`[DEFAULT]` block::

	user_devices = naqs_devices_template_device

If more than one module of 3rd party devices are used, put all module names
as a comma separated list.


Usage
=====

Invoke in labscript scripts just like other labscript devices::

	from naqs_devices_template import HelperClass
	from naqs_devices_template.TemplateDevice.labscript_device import TemplateDevice

Details for how to use each device are contained in the :doc:`detailed documentation <devices>` listings.