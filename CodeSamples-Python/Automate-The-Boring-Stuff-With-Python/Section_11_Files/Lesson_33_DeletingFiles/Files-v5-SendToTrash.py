# os.unlink() will delete a file.
# os.rmdir() will delete a folder (but the folder must be empty).
# shutil.rmtree() will delete a folder and all its contents.
# Deleting can be dangerous, so do a "dry run" first.
# send2trash.send2trash() will send a file or folder to the recycling bin.

# Import relevant Modules
import send2trash, shutil

# Create a Sample Text File utilizing shutil.copy() to then Delete; 1st argument = From Directory XYZ, 2nd argument = To Directory XYZ AND (optional) rename by inputting a new File name value after the To Directory
shutil.copy('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_31_ReadingWritingPlaintextFiles\\Hello.txt', 'C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_33_DeletingFiles\\hellohellohello.txt')

# Delete a Local file by sending it to the recycling bin utilizing send2trash.send2trash()
send2trash.send2trash('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_33_DeletingFiles\\hellohellohello.txt')
        