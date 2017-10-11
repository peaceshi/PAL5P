import sys
import os.path


def set_dir(string):
    working_dir = sys.path[0] + string
    if not os.path.exists(working_dir):
        print("\"", working_dir, "\"", 'path not exits or fail to access.')
        return sys.exit(1)
    return working_dir
# set_dir(string)


def get_file_names(get_dir):
    for dirpath, dirnames, filenames in os.walk(get_dir):
        names = filenames
    return names
# get_file_names(get_dir)


