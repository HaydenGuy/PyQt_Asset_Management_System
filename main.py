import os
import sys
import datetime
import humanize
import stat

from PySide2.QtWidgets import QMainWindow, QApplication
from UI.Ui_asset_management import Ui_asset_management

# Class to define an asset
class Asset:
    def __init__(self, name, extension, type):
        self.name = name
        self.extension = extension
        self.type = type

    def __str__(self):
        return f'{self.name} | {self.extension} | {self.type}'

# Class to define asset categories
class Asset_Category:
    def __init__(self):
        self.assets = []

    # Add an asset to the category by adding to the assets list
    def add_asset(self, asset, metadata):
        self.assets.append([asset, metadata])

    # Remove an asset and its metadata by iterating through the assets list and removing a matched item
    def remove_asset(self, remove_asset):
        for asset, metadata in self.assets:
            if asset.name == remove_asset:
                self.assets.remove([asset, metadata])
    
    # Returns the assets list
    def list_assets(self):
        return self.assets
    

class name(QMainWindow, Ui_asset_management):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# Gets the file size and uses humanize to put it in readable format
def get_file_size(file):
    file_size = os.path.getsize(file)
    file_size_readable = humanize.naturalsize(file_size)

    return file_size_readable

# Gets the file creation time and uses datetime to put it in readable format
def get_file_creation_time(file):
    file_creation_time = os.path.getctime(file)
    creation_time_readable = datetime.datetime.fromtimestamp(
        file_creation_time).strftime('%Y_%m_%d_%H_%M_%S')

    return creation_time_readable

# Gets the file modification time and uses datetime to put it in readable format
def get_file_modification_time(file):
    file_modification_time = os.path.getmtime(file)
    modification_time_readable = datetime.datetime.fromtimestamp(
        file_modification_time).strftime('%Y_%m_%d_%H_%M_%S')
    
    return modification_time_readable

# Gets the file permissions and uses stat to put it in readable format
def get_file_permissions(file):
    file_permissions = os.stat(file).st_mode
    file_permissions_readable = stat.filemode(file_permissions)

    return file_permissions_readable

# Add the files metadata to a list
def get_metadata(file):
    file_metadata = []

    file_metadata.append(get_file_size(file))
    file_metadata.append(get_file_creation_time(file))
    file_metadata.append(get_file_modification_time(file))
    file_metadata.append(get_file_permissions(file))

    return file_metadata

# Gets the file name, extension, and what type of file it is
def get_file_details(file):
    file_name, file_extension = os.path.splitext(file)

    if file_extension in video_formats:
        file_type = "video"
    elif file_extension in text_formats:
        file_type = "text"
    elif file_extension in image_formats:
        file_type = "image"
    elif file_extension in model_formats:
        file_type = "model"
    elif file_extension in production_formats:
        file_type = "production"

    return file_name, file_extension, file_type

def create_asset(file):
    name, extension, type = get_file_details(file)
    asset = Asset(name, extension, type)
    
    return asset

# Sets containing common file formats
video_formats = {'.mp4', '.avi', '.mov',
                 '.mkv', '.wmv', '.flv', '.webm', '.mpeg'}
text_formats = {'.txt', '.csv', '.json', '.xml', '.html', '.pdf'}
image_formats = {'.jpg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.exr'}
model_formats = {'.fbx', '.obj', '.stl', '.dae', '.blend'}
production_formats = {'.usd', '.ma', '.mb', '.uasset',
                      '.psd', '.ai', '.prproj', '.aep', '.drp'}


# TEMPORARY CODE - to be deleted/reworked
os.chdir('testing')
current_dir = os.getcwd()
file_list = os.listdir(current_dir)

video_assets = Asset_Category()
text_assets = Asset_Category()
image_assets = Asset_Category()
model_assets = Asset_Category()
production_assets = Asset_Category()

# Adds files in the current directory to the asset class 
for file in file_list:
    asset = create_asset(file)
    metadata = get_metadata(file)
     
    if asset.type == "video":
        video_assets.add_asset(asset, metadata)
    elif asset.type == "text":
        text_assets.add_asset(asset, metadata)
    elif asset.type == "image":
        image_assets.add_asset(asset, metadata)
    elif asset.type == "model":
        model_assets.add_asset(asset, metadata)
    elif asset.type == "production":
        production_assets.add_asset(asset, metadata)


for asset, metadata in video_assets.list_assets():
    print(asset, metadata)

# for asset, metadata in text_assets.list_assets():
#     print(asset, metadata)

# for asset, metadata in image_assets.list_assets():
#     print(asset, metadata)

# for asset, metadata in model_assets.list_assets():
#     print(asset, metadata)

# for asset, metadata in production_assets.list_assets():
#     print(asset, metadata)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = name()
    window.show()

    sys.exit(app.exec_())