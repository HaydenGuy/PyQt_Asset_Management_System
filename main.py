import os
import datetime
import humanize
import stat

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
    def add_asset(self, asset):
        self.assets.append(asset)

    # Remove an asset by iterating through the assets list and removing a matched item
    def remove_asset(self, remove_asset):
        for asset in self.assets:
            if asset.name == remove_asset:
                self.assets.remove(asset)
                return f"Removed: {asset}"
    
    # Returns the assets list
    def list_assets(self):
        return self.assets
        
# Get the metadata from a file
def get_metadata(file):
    # Gets the file size and uses humanize to put it in readable format
    file_size = os.path.getsize(file)
    file_size_readable = humanize.naturalsize(file_size)

    # Gets the file creation time and uses datetime to put it in readable format
    file_creation_time = os.path.getctime(file)
    creation_time_readable = datetime.datetime.fromtimestamp(
        file_creation_time).strftime('%Y_%m_%d_%H_%M_%S')

    # Gets the file modification time and uses datetime to put it in readable format
    file_modification_time = os.path.getmtime(file)
    modification_time_readable = datetime.datetime.fromtimestamp(
        file_modification_time).strftime('%Y_%m_%d_%H_%M_%S')

    # Gets the file permissions and uses stat to put it in readable format
    file_permissions = os.stat(file).st_mode
    file_permissions_readable = stat.filemode(file_permissions)

    return file_size_readable, creation_time_readable, modification_time_readable, file_permissions_readable

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


# TEMPORARY CODE
os.chdir('testing')
current_dir = os.getcwd()
file_list = os.listdir(current_dir)

video_assets = Asset_Category()
text_assets = Asset_Category()
image_assets = Asset_Category()
model_assets = Asset_Category()
production_assets = Asset_Category()

for file in file_list:
    asset = create_asset(file)
    
    if asset.type == "video":
        video_assets.add_asset(asset)
    elif asset.type == "text":
        text_assets.add_asset(asset)
    elif asset.type == "image":
        image_assets.add_asset(asset)
    elif asset.type == "model":
        model_assets.add_asset(asset)
    elif asset.type == "production":
        production_assets.add_asset(asset)

for asset in video_assets.list_assets():
    print(asset)

# for asset in production_assets.list_assets():
#     print(asset)