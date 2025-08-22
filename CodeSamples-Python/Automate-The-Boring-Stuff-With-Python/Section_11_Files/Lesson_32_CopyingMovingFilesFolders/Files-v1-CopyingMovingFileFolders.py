# Import relevant Modules
import shutil

# Specify a file to Copy utilizing shutil.copy(); 1st argument = From, 2nd argument = To
shutil.copy('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_31_ReadingWritingPlaintextFiles\\Hello.txt', 'C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_32_CopyingMovingFilesFolders')

# Specify a file to Copy utilizing shutil.copy(); 1st argument = From Directory XYZ, 2nd argument = To Directory XYZ AND (optional) rename by inputting a new File name value after the To Directory
shutil.copy('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_31_ReadingWritingPlaintextFiles\\Hello.txt', 'C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_32_CopyingMovingFilesFolders\\hellohellohello.txt')

# Specify a Folder, and all its content, to Copy utilizing shutil.copytree(); 1st argument = From Directory XYZ, 2nd argument = To Directory XYZ AND (optional) rename by inputting a new File name value after the To Directory
shutil.copytree('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_31_ReadingWritingPlaintextFiles', 'C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_32_CopyingMovingFilesFolders\\Lesson_31_Backup')

# Specify a file to Move utilizing shutil.move(); 1st argument = From Directory XYZ, 2nd argument = To Directory XYZ AND (optional) rename by inputting a new File name after the To Directory XYZ value
shutil.move('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_32_CopyingMovingFilesFolders\\hellohellohello.txt', 'C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_31_ReadingWritingPlaintextFiles')