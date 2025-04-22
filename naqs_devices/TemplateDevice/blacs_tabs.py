from blacs.device_base_class import DeviceTab, define_state, MODE_BUFFERED

class TemplateDeviceTab(DeviceTab):
    def initialise_workers(self):
        worker_initialisation_kwargs = {}
        self.create_worker(
            "main_worker",
            "naqs_devices.TemplateDevice.blacs_workers.TemplateDeviceWorker",
            worker_initialisation_kwargs,
        )
        self.primary_worker = "main_worker"

    @define_state(MODE_BUFFERED, True)
    def start_run(self, notify_queue):
        self.wait_until_done(notify_queue)

    @define_state(MODE_BUFFERED, True)
    def wait_until_done(self, notify_queue):
        """
        Call check_if_done repeatedly in the worker until the shot is 
        complete
        """
        done = yield (self.queue_work(self.primary_worker, 'check_if_done'))
        # Experiment is over. Tell the queue manager about it:
        if done:
            notify_queue.put('done')
        else:
            # Not actual recursion since this just queues up another call
            # after we return:
            self.wait_until_done(notify_queue)
    