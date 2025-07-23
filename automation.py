import os
import shutil

# Source and destination folder paths
source_folder = r'D:\caJPGfile'
destination_folder = r'D:\caJPGfile2'

# Creating the destination folder
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# File search
for filename in os.listdir(source_folder):
    if filename.lower().endswith('.jpg'):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        # Moving the .jpg file
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename}")

print("All .jpg files have been moved successfully.")
