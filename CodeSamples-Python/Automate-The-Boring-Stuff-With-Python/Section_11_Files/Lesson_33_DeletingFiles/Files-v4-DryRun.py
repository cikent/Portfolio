# os.unlink() will delete a file.
# os.rmdir() will delete a folder (but the folder must be empty).
# shutil.rmtree() will delete a folder and all its contents.
# Deleting can be dangerous, so do a "dry run" first.
# send2trash.send2trash() will send a file or folder to the recycling bin.

# Import relevant Modules
import os, shutil

# Change the working directory
os.chdir('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_32_CopyingMovingFilesFolders')

# Create a program to perform a Dry Run before accidently deleting Files & Folders permanently
for filename in os.listdir():
    if filename.endswith('.rxt'):
        # os.unlink(filename)
        print(filename)
        