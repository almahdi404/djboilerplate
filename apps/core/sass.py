import os
import site
import threading
import time
from pathlib import Path

import sass
from django.apps import apps
from django.conf import settings


def compiler():
    packageFolders = [
        site.getusersitepackages(),
        *[path for path in site.getsitepackages()],
    ]

    staticFolders = settings.STATICFILES_DIRS.copy()
    staticFolders += [
        os.path.join(app.path, "static") for app in apps.get_app_configs()
    ]

    compileFolders = staticFolders.copy()
    for staticFolder in staticFolders:
        for packageFolder in packageFolders:
            if Path(staticFolder).is_relative_to(packageFolder):
                if staticFolder in compileFolders:
                    compileFolders.remove(staticFolder)

    if settings.DEBUG:
        from watchdog.events import FileSystemEvent, FileSystemEventHandler
        from watchdog.observers import Observer

        def watcher(path):
            class EventHandler(FileSystemEventHandler):
                def dispatch(self, event: FileSystemEvent):
                    if event.event_type == "closed":
                        filename, extension = os.path.splitext(event.src_path)
                        if extension == ".scss":
                            time.sleep(0.5)
                            for d in compileFolders:
                                if os.path.isdir(d):
                                    try:
                                        sass.compile(
                                            dirname=(d, d),
                                            output_style="expanded",
                                            include_paths=staticFolders,
                                        )
                                    except sass.CompileError as error:
                                        print(error)

            event_handler = EventHandler()
            observer = Observer()
            observer.schedule(event_handler, path, recursive=True)
            observer.start()
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                observer.stop()
            observer.join()

        for d in compileFolders:
            if os.path.isdir(d):
                try:
                    sass.compile(
                        dirname=(d, d),
                        output_style="expanded",
                        include_paths=staticFolders,
                    )
                except sass.CompileError as error:
                    print(error)
                thread = threading.Thread(target=watcher, args=(d,), daemon=True)
                thread.start()
    else:
        d = settings.STATIC_ROOT
        if os.path.exists(d):
            try:
                sass.compile(
                    dirname=(d, d),
                    output_style="expanded",
                    include_paths=staticFolders,
                )
            except sass.CompileError as error:
                print(error)
