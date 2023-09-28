import os
import datetime
import humanize
import stat

# Class to define an asset
class Asset:
    def __init__(self, name, type, extension):
        self.name = name
        self.type = type
        self.extension = extension

# Get the metadata from a file
def get_metadata(file):
    # Gets the file size and uses humanize to put it in readable format
    file_size = os.path.getsize(file)
    file_size_readable = humanize.naturalsize(file_size)

    # Gets the file creation time and uses datetime to put it in readable format
    file_creation_time = os.path.getctime(file)
    creation_time_readable = datetime.datetime.fromtimestamp(file_creation_time).strftime('%Y_%m_%d_%H_%M_%S')

    # Gets the file modification time and uses datetime to put it in readable format
    file_modification_time = os.path.getmtime(file)
    modification_time_readable = datetime.datetime.fromtimestamp(file_modification_time).strftime('%Y_%m_%d_%H_%M_%S')

    # Gets the file permissions and uses stat to put it in readable format
    file_permissions = os.stat(file).st_mode
    file_permissions_readable = stat.filemode(file_permissions)

    return file_size_readable, creation_time_readable, modification_time_readable, file_permissions_readable

# Gets the files name and extension
def get_file_name_extension(file):
    file_name = os.path.splitext(file)[0]

    file_extension = os.path.splitext(file)[1]

    return file_name, file_extension


# TEMPORARY CODE
os.chdir("testing")
current_dir = os.getcwd()
file_list = os.listdir(current_dir)

for file in file_list:
    print(get_file_name_extension(file))