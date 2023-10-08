#!/usr/bin/python3.10

import os
import sys
import datetime, humanize, stat

from PySide2.QtWidgets import QMainWindow, QApplication, QListWidgetItem
from UI.Ui_asset_management import Ui_asset_management

# Class to define an asset
class Asset:
    def __init__(self, name, extension, type):
        self.name = name
        self.extension = extension
        self.type = type

    def __str__(self):
        return f'{self.name}{self.extension}'

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

        # Sets containing common file formats
        self.video_formats = {'.mp4', '.avi', '.mov',
                         '.mkv', '.wmv', '.flv', '.webm', '.mpeg'}
        self.text_formats = {'.txt', '.csv', '.json', '.xml', '.html', '.pdf'}
        self.image_formats = {'.jpg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.exr'}
        self.model_formats = {'.fbx', '.obj', '.stl', '.dae', '.blend'}
        self.production_formats = {'.usd', '.ma', '.mb', '.uasset',
                              '.psd', '.ai', '.prproj', '.aep', '.drp'}
        
        # Uses the Asset_Catergory class to define each category
        self.video_assets = Asset_Category()
        self.text_assets = Asset_Category()
        self.image_assets = Asset_Category()
        self.model_assets = Asset_Category()
        self.production_assets = Asset_Category()

        self.populate_lists()


    # Gets the file size and uses humanize to put it in readable format
    def get_file_size(self, file):
        file_size = os.path.getsize(file)
        file_size_readable = humanize.naturalsize(file_size)

        return file_size_readable

    # Gets the file creation time and uses datetime to put it in readable format
    def get_file_creation_time(self, file):
        file_creation_time = os.path.getctime(file)
        creation_time_readable = datetime.datetime.fromtimestamp(
            file_creation_time).strftime('%Y_%m_%d_%H_%M_%S')

        return creation_time_readable

    # Gets the file modification time and uses datetime to put it in readable format
    def get_file_modification_time(self, file):
        file_modification_time = os.path.getmtime(file)
        modification_time_readable = datetime.datetime.fromtimestamp(
            file_modification_time).strftime('%Y_%m_%d_%H_%M_%S')
        
        return modification_time_readable

    # Gets the file permissions and uses stat to put it in readable format
    def get_file_permissions(self, file):
        file_permissions = os.stat(file).st_mode
        file_permissions_readable = stat.filemode(file_permissions)

        return file_permissions_readable

    # Add the files metadata to a list
    def get_metadata(self, file):
        file_metadata = []

        file_metadata.append(self.get_file_size(file))
        file_metadata.append(self.get_file_creation_time(file))
        file_metadata.append(self.get_file_modification_time(file))
        file_metadata.append(self.get_file_permissions(file))

        return file_metadata

    # Gets the file name, extension, and what type of file it is
    def get_file_details(self, file):
        file_name, file_extension = os.path.splitext(file)

        if file_extension in self.video_formats:
            file_type = "video"
        elif file_extension in self.text_formats:
            file_type = "text"
        elif file_extension in self.image_formats:
            file_type = "image"
        elif file_extension in self.model_formats:
            file_type = "model"
        elif file_extension in self.production_formats:
            file_type = "production"
        else:
            file_type = "unknown"

        return file_name, file_extension, file_type

    # Creates an asset using the Asset class
    def create_asset(self, file):
        name, extension, type = self.get_file_details(file)
        asset = Asset(name, extension, type)
        
        return asset
    
    # Populate the UI tab lists based on the files found in the folder 
    def populate_lists(self):
        # Adds files in the current directory to the asset class 
        for file in file_list:
            asset = self.create_asset(file)
            metadata = self.get_metadata(file)
            
            if asset.type == "video":
                self.video_assets.add_asset(asset, metadata)
                list_item = QListWidgetItem(f"{asset} \n {metadata}")
                self.video_list.addItem(list_item)

            elif asset.type == "text":
                self.text_assets.add_asset(asset, metadata)
                list_item = QListWidgetItem(f"{asset} \n {metadata}")
                self.text_list.addItem(list_item)

            elif asset.type == "image":
                self.image_assets.add_asset(asset, metadata)
                list_item = QListWidgetItem(f"{asset} \n {metadata}")
                self.image_list.addItem(list_item)

            elif asset.type == "model":
                self.model_assets.add_asset(asset, metadata)
                list_item = QListWidgetItem(f"{asset} \n {metadata}")
                self.model_list.addItem(list_item)

            elif asset.type == "production":
                self.production_assets.add_asset(asset, metadata)
                list_item = QListWidgetItem(f"{asset} \n {metadata}")
                self.production_list.addItem(list_item)

# Uses os.walk to check subfolders for files
def list_files_recursively(root_dir):
    file_list = []

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_list.append(os.path.join(root, file))

    return file_list

# Fix issue with recursion
if __name__ == '__main__':
    if len(sys.argv) < 2:
        folder_path = os.getcwd()
    else:
        os.chdir(sys.argv[1])
        folder_path = os.getcwd()

    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        file_list = list_files_recursively(folder_path)
    else:
        print("Invalid path", file=sys.stderr)

    app = QApplication(sys.argv)

    window = name()
    window.show()

    sys.exit(app.exec_())