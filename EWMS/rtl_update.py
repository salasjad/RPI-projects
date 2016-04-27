import time
import threading

class rtl_load(object):
    def __init__(self, interval=0.1):
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            print('Thread execution')

            time.sleep(self.interval)
