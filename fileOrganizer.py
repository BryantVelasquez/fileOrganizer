import os
import shutil

# 1. Ask the user for the folder they want to organize
path = input("Enter Path: ")

# 2. Get a list of everything in that folder
files = os.listdir(path)

# 3. Loop over each item in the folder
for file in files:
    # 3a. Split “name” and “.extension”
    filename, extension = os.path.splitext(file)
    # 3b. Remove the leading dot (so “.pdf” → “pdf”)
    extension = extension[1:]
    
    # 4. Build the full paths we’ll need
    src      = os.path.join(path, file)
    dest_dir = os.path.join(path, extension)
    dest     = os.path.join(dest_dir, file)

    # 5. If a folder for this extension already exists…
    if os.path.exists(dest_dir):
        # …just move the file into it
        shutil.move(src, dest)
    else:
        # 6. Otherwise, make that folder…
        os.makedirs(dest_dir)
        # …and then move the file
        shutil.move(src, dest)
