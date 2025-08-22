# os.unlink() will delete a file.
# os.rmdir() will delete a folder (but the folder must be empty).
# shutil.rmtree() will delete a folder and all its contents.
# Deleting can be dangerous, so do a "dry run" first.
# send2trash.send2trash() will send a file or folder to the recycling bin.

# Import relevant Modules
import os

# Specify a Folder to Delete utilizing os.rmdir(); The Folder MUST be empty otherwise an Error will be returned
os.rmdir('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_33_DeletingFiles')