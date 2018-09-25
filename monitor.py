import os, time
import datetime
import importlib.util


#spec_sync = importlib.util.spec_from_file_location("module.name", "E:\Research\sync_detect\sync_detect.py" )
#foo_sync = importlib.util.module_from_spec(spec_sync)
#spec_sync.loader.exec_module(foo_sync)

path_to_watch = "C:\\Users\ARJ\Dropbox"
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
    time.sleep (10)
    after = dict([(f, None) for f in os.listdir (path_to_watch)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]

    if added:
        print("Added: ", ", ".join (added))
        os.system('python sync_detect.py')
    if removed:
        print("Removed: ", ", ".join(removed))
    before = after
