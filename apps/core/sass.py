import os
import glob
import time
import sass
import logging
import threading
from django.conf import settings
from watchdog.observers import Observer
from watchdog.events import FileModifiedEvent


def compiler():
    BASE_DIR = str(settings.BASE_DIR)
    staticFolders = glob.glob(os.path.join(BASE_DIR, "apps", "**", "static"))
    staticFolders += settings.STATICFILES_DIRS

    if settings.DEBUG:
        def compile(path):
            class Event(FileModifiedEvent):
                def dispatch(self, event):
                    filename, extension = os.path.splitext(event.src_path)
                    if extension == ".scss":
                        d = os.path.dirname(event.src_path)
                        time.sleep(0.1)
                        sass.compile(dirname=(d, d), output_style="expanded")

            logging.basicConfig(level=logging.INFO,
                                format='%(asctime)s - %(message)s',
                                datefmt='%Y-%m-%d %H:%M:%S')
            event_handler = Event(path)
            observer = Observer()
            observer.schedule(event_handler, path, recursive=True)
            observer.start()
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                observer.stop()
            observer.join()

        for d in staticFolders:
            if os.path.isdir(d):
                sass.compile(dirname=(d, d), output_style="expanded")
                thread = threading.Thread(
                    target=compile, args=(d,), daemon=True)
                thread.start()
    else:
        d = settings.STATIC_ROOT
        if os.path.exists(d):
            sass.compile(dirname=(d, d), output_style="expanded")
