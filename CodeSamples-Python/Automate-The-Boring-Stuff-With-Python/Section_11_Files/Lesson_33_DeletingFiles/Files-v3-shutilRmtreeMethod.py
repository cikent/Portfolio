# os.unlink() will delete a file.
# os.rmdir() will delete a folder (but the folder must be empty).
# shutil.rmtree() will delete a folder and all its contents.
# Deleting can be dangerous, so do a "dry run" first.
# send2trash.send2trash() will send a file or folder to the recycling bin.

# Import relevant Modules
import shutil

# Create a Sample Folder Structure to then delete utilizing shutil.copytree(); 1st argument = From Directory XYZ, 2nd argument = To Directory XYZ AND (optional) rename by inputting a new File name value after the To Directory
shutil.copytree('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_33_DeletingFiles', 'C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_33_DeletingFiles\\Lesson_33_DeletingFiles-TestBackupToDelete')

# Specify a Folder to Delete utilizing shutil.rmtree() will delete a folder and all its contents.
shutil.rmtree('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_33_DeletingFiles\\Lesson_33_DeletingFiles-TestBackupToDelete')