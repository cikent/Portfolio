# os.unlink() will delete a file.
# os.rmdir() will delete a folder (but the folder must be empty).
# shutil.rmtree() will delete a folder and all its contents.
# Deleting can be dangerous, so do a "dry run" first.
# send2trash.send2trash() will send a file or folder to the recycling bin.

# Import relevant Modules
import os, shutil

# Update the variable value
debugVar_OSGetCwd = os.getcwd()

# Print Debug Variable again
print(debugVar_OSGetCwd)

# Specify a file to Move utilizing shutil.move(); 1st argument = From Directory XYZ, 2nd argument = To Directory XYZ AND (optional) rename by inputting a new File name after the To Directory XYZ value
shutil.move('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_31_ReadingWritingPlaintextFiles\\hellohellohello.txt', 'C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python')

# Delete a file utilizing os.unlink() from the current working directory
os.unlink('hellohellohello.txt')