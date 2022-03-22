import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Exeventhandler(FileSystemEventHandler):
    def on_created(self, event):
        return super().on_created(event)


observer = Observer()
event_handler = Exeventhandler() # create event handler
# set observer to use created handler in directory
observer.schedule(event_handler, path='/folder/to/watch')
observer.start()

# sleep until keyboard interrupt, then stop + rejoin the observer
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()