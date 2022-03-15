from lib2to3.pygram import pattern_symbols
from msilib.schema import File
import sys
import time
import logging
from watchdog.observers import Observer  #creating an instance of the watchdog.observers.Observer from watchdogs class.
from watchdog.events import FileCreatedEvent  #implementing a subclass of watchdog.events.FileSystemEventHandler which is LoggingEventHandler in our case

if __name__ == "__main__":
    path = (r'C:\\Code Projects\\Clip-Automation')
    my_event_handler = FileCreatedEvent(path)
    observer = Observer()
    observer.schedule(my_event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()