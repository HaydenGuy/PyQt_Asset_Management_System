#!/usr/bin/python3.10

import os
import sys
import datetime
import humanize
import stat

from PySide2.QtWidgets import QMainWindow, QApplication, QListWidgetItem, QFileDialog
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
        self.video_formats = ('.mp4', '.avi', '.mov',
                              '.mkv', '.wmv', '.flv', '.webm', '.mpeg')
        self.text_formats = ('.txt', '.csv', '.pdf', '.json', '.xml', '.html')
        self.image_formats = ('.jpg', '.png',
                              '.gif', '.bmp', '.tiff', '.svg', '.exr')
        self.model_formats = ('.fbx', '.obj', '.stl', '.dae', '.blend')
        self.production_formats = ('.usd', '.ma', '.mb', '.uasset',
                                   '.psd', '.ai', '.prproj', '.aep', '.drp')

        # Uses the Asset_Catergory class to define each category
        self.video_assets = Asset_Category()
        self.text_assets = Asset_Category()
        self.image_assets = Asset_Category()
        self.model_assets = Asset_Category()
        self.production_assets = Asset_Category()

        self.current_folder_path = initial_folder_path

        # Initialization modules for the UI and UI controls
        self.populate_lists(self.current_folder_path)
        self.updateUI()
        self.tab_changed()

    # Controls the logic for when the reload button is pressed or the tab is changed
    def updateUI(self):
        self.pb_reload.pressed.connect(self.reload_ui)
        self.tabWidget.currentChanged.connect(self.tab_changed)
        self.pb_browse.pressed.connect(self.browse_folders)

    # Gets the file list from the folder path given in the main block
    def get_file_list(self, folder_path):
        self.file_list = []

        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    self.file_list.append(os.path.join(root, file))
        else:
            print("Invalid path", file=sys.stderr)

        return self.file_list

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
        file_path, file_extension = os.path.splitext(file)

        split_name = file_path.split('/')
        file_name = split_name[-1]

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
    def populate_lists(self, folder_path):
        file_list = sorted(self.get_file_list(folder_path))

        # Adds files in the current directory to the asset class
        for file in file_list:
            asset = self.create_asset(file)
            metadata = self.get_metadata(file)

            if asset.type == "video":
                self.video_assets.add_asset(asset, metadata)
                list_item = QListWidgetItem(
                    f"{asset} \n {metadata[0]} \n Creation time: {metadata[1]} \n Modification time: {metadata[2]} \n Permissions: {metadata[3]} \n {file} \n")
                self.video_list.addItem(list_item)

            elif asset.type == "text":
                self.text_assets.add_asset(asset, metadata)
                list_item = QListWidgetItem(
                    f"{asset} \n {metadata[0]} \n Creation time: {metadata[1]} \n Modification time: {metadata[2]} \n Permissions: {metadata[3]} \n {file} \n")
                self.text_list.addItem(list_item)

            elif asset.type == "image":
                self.image_assets.add_asset(asset, metadata)
                list_item = QListWidgetItem(
                    f"{asset} \n {metadata[0]} \n Creation time: {metadata[1]} \n Modification time: {metadata[2]} \n Permissions: {metadata[3]} \n {file} \n")
                self.image_list.addItem(list_item)

            elif asset.type == "model":
                self.model_assets.add_asset(asset, metadata)
                list_item = QListWidgetItem(
                    f"{asset} \n {metadata[0]} \n Creation time: {metadata[1]} \n Modification time: {metadata[2]} \n Permissions: {metadata[3]} \n {file} \n")
                self.model_list.addItem(list_item)

            elif asset.type == "production":
                self.production_assets.add_asset(asset, metadata)
                list_item = QListWidgetItem(
                    f"{asset} \n {metadata[0]} \n Creation time: {metadata[1]} \n Modification time: {metadata[2]} \n Permissions: {metadata[3]} \n {file} \n")
                self.production_list.addItem(list_item)

    # Reload the UI by clearing the exisiting lists and repopulating
    def reload_ui(self):
        self.file_list = []
        self.video_list.clear()
        self.text_list.clear()
        self.image_list.clear()
        self.model_list.clear()
        self.production_list.clear()
        self.populate_lists(self.current_folder_path)

    # Updates the bottom text to show the file formats being searched when the tab is changed
    def tab_changed(self):
        current_tab_index = self.tabWidget.currentIndex()
        current_tab_name = self.tabWidget.tabText(current_tab_index)

        if current_tab_name == "Video":
            self.lb_file_formats.setText('  '.join(map(str, self.video_formats)))
        elif current_tab_name == "Text":
            self.lb_file_formats.setText('  '.join(map(str, self.text_formats)))
        elif current_tab_name == "Image":
                    self.lb_file_formats.setText('  '.join(map(str, self.image_formats)))
        elif current_tab_name == "Model":
                    self.lb_file_formats.setText('  '.join(map(str, self.model_formats)))
        elif current_tab_name == "Production":
                    self.lb_file_formats.setText('  '.join(map(str, self.production_formats)))

    # Updates the current folder path and allows the user to open a folder using File>Open
    def browse_folders(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", options=options)

        self.current_folder_path = folder_path

        if folder_path:
            self.reload_ui()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        initial_folder_path = os.getcwd()
    else:
        os.chdir(sys.argv[1])
        initial_folder_path = os.getcwd()

    app = QApplication(sys.argv)

    window = name()
    window.show()

    sys.exit(app.exec_())
