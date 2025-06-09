from blacs.device_base_class import DeviceTab, define_state, MODE_BUFFERED

class TemplateDeviceTab(DeviceTab):

    show_widgets = True

    def initialise_GUI(self):
        '''Required to place GUI widgets and contains options for remote value
        checking and smart cache capability.
        '''

        # Capabilities
        self.base_units =    {'freq':'Hz',          'amp':'Arb',   'phase':'Degrees'}
        self.base_min =      {'freq':0.0,           'amp':0,       'phase':0}
        self.base_max =      {'freq':250.0 * 10**6, 'amp':1,       'phase':360}
        self.base_step =     {'freq':10**6,         'amp':1/1023., 'phase':1}
        self.base_decimals = {'freq':1,             'amp':4,       'phase':3}
        self.num_DDS = 4
        self.num_AO = 3

        if self.show_widgets:

            # Example of DDS widget construction
            dds_prop = {}
            for i in range(self.num_DDS):
                dds_prop['channel %d' % i] = {}
                for subchnl in ['freq', 'amp', 'phase']:
                    dds_prop['channel %d' % i][subchnl] = {'base_unit':self.base_units[subchnl],
                                                        'min':self.base_min[subchnl],
                                                        'max':self.base_max[subchnl],
                                                        'step':self.base_step[subchnl],
                                                        'decimals':self.base_decimals[subchnl]
                                                        }
            self.create_dds_outputs(dds_prop)
                    
            # Example of AO widget construction
            ao_prop = {'tau':{'base_unit':'s',
                            'min':1e-6,
                            'max':30e3,
                            'step':1,
                            'decimals':6},
                        'sens':{'base_unit':'V',
                                'min':1e-9,
                                'max':1,
                                'step':1e-3,
                                'decimals':9},
                        'phase':{'base_unit':'deg',
                                'min':-180,
                                'max':180,
                                'step':1,
                                'decimals':6}}
            
            self.create_analog_outputs(ao_prop)
            
            # Example of DO widget construction
            do_prop = {}
            for i in range(0, 5):
                do_prop['do{:01d}'.format(i)] = {}
            self.create_digital_outputs(do_prop)

            def sort(channel):
                return int(channel.split('do')[-1])
                                
            
            dds_widgets, ao_widgets, do_widgets = self.auto_create_widgets()
            self.auto_place_widgets(
                ('DDS Outputs', dds_widgets), 
                ('Analog Outputs', ao_widgets),
                ('Digital Outputs', do_widgets, sort)
                )

            # # Example of Enum widget construction
            # eo_prop = {
            #     'Enum1':{
            #         'options':['option 1', 'option 2', 'option 3'], # uses default 0-indexing
            #         'return_index':True, # widget will return integer index instead of string value when queried
            #     },
            #     'Enum2':{
            #         'options':{
            #             'option 1':{'index':2, 'tooltip':'description 1'},
            #             'option 2':4, # if tooltip not desired, just pass custom index
            #             'option 3':5
            #         }
            #     },
            #     'Setting3':{
            #         'options': ['On', 'Off'],
            #         'return_index':True
            #     }
            # }
            # self.create_enum_outputs(eo_prop)
            # eo_widgets = self.auto_create_enum_widgets()

            # self.auto_place_widgets(('Enums', eo_widgets))


        self.supports_remote_value_check(False)
        self.supports_smart_programming(True)

    def initialise_workers(self):
        '''Starts the workers, which handle communications between front panel,
        shot-file, and labscript instructions.
        '''
        worker_initialisation_kwargs = {}
        self.create_worker(
            "main_worker",
            "naqs_devices.TemplateDevice.blacs_workers.TemplateDeviceWorker",
            worker_initialisation_kwargs,
        )
        self.primary_worker = "main_worker"

    @define_state(MODE_BUFFERED, True)
    def start_run(self, notify_queue):
        '''Tab's method to enforce that, once the run is started, updates only
        happen after run ends by calling :meth:`wait_until_done`()
        '''
        self.wait_until_done(notify_queue)

    @define_state(MODE_BUFFERED, True)
    def wait_until_done(self, notify_queue):
        '''Call check_if_done repeatedly in the worker until the shot is complete'''
        done = yield (self.queue_work(self.primary_worker, 'check_if_done'))
        # Experiment is over. Tell the queue manager about it:
        if done:
            notify_queue.put('done')
        else:
            # Not actual recursion since this just queues up another call
            # after we return:
            self.wait_until_done(notify_queue)