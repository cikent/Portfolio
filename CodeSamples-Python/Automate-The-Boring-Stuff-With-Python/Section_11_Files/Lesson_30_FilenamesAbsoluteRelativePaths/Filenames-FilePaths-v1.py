# Files have a name and a path.
# The root folder is the lowest folder.
# In a file path, the folders and filename are separated by backslashes on Windows and forward slashes on Linux and Mac.
# Use the os.path.join() function to combine folders with the correct slash.
# The current working directory is the oflder that any relative paths are relative to.
# os.getcwd() will return the current working directory.
# os.chdir() will change the current working directory.
# Absolute paths begin with the root folder, relative paths do not.
# The . folder represents "this folder", the .. folder represents "the parent folder".
# os.path.abspath() returns an absolute path form of the path passed to it.
# os.path.relpath() returns the relative path between two paths passed to it.
# os.makedirs() can make folders.
# os.path.getsize() returns a file's size.
# os.listdir() returns a list of strings of filenames.
# os.path.exists() returns True if the filename passed to it exists.
# os.path.isfile() and os.path.isdir() return True if they were passed a filename or file path.

# Import relevant modules
import os

# Create a Debug Variable for os.path.join(), to return a string 
debugVar_OSPathJoinPathVar = os.path.join('folder1', 'folder2', 'folder3', 'file.png')

# Print Debug Variable
print(debugVar_OSPathJoinPathVar)

# Create a Debug Variable for os.getcwd(), to return the Current Working Directory
debugVar_OSGetCwd = os.getcwd()

# Print Debug Variable
print(debugVar_OSGetCwd)

# Change Working Directory
os.chdir('c:\\')

# Update the variable value
debugVar_OSGetCwd = os.getcwd()

# Print Debug Variable again
print(debugVar_OSGetCwd)

# Change Working Directory
os.chdir('c:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python')

# Update the variable value
debugVar_OSGetCwd = os.getcwd()

# Print Debug Variable again
print(debugVar_OSGetCwd)

# Create a Debug Variable for os.path.abspath(), to return the Absolute Path for a value passed
debugVar_AbsPath = os.path.abspath('spam.png')

# Print Debug Variable
print(debugVar_AbsPath)

# Create a Debug Variable for os.path.isabs(), to return a Boolean value based upon whether or not the Path value passed is indeed correct
debugVar_IsAbsFalse = os.path.isabs('spam.png')
debugVar_IsAbsTrue = os.path.isabs('c:\Development\Python-Projects\Automate-The-Boring-Stuff-With-Python\spam.png')

# Print Debug Variable
print(debugVar_IsAbsFalse)
print(debugVar_IsAbsTrue)

# Create a Debug Variable for os.path.relpath(), to return a relative path value, which is relative to the program’s current working directory
debugVar_RelPath = os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder1')

# Print Debug Variable
print(debugVar_RelPath)

# Create a Debug Variable for os.path.dirname(), to return the directory path for a Path value passed
debugVar_DirName = os.path.dirname('c:\\folder1\\folder2\\spam.png')

# Print Debug Variable
print(debugVar_DirName)

# Create a Debug Variable for os.path.basename(), to return the last folder/file for a Path value passed
debugVar_BaseName = os.path.basename('c:\\folder1\\folder2\\spam.png')

# Print Debug Variable
print(debugVar_BaseName)

# Create a Debug Variable for os.path.exists(), to return a Boolean value based upon whether or not the Path value passed does indeed exist
debugVar_ExistsFalse = os.path.exists('c:\Development\Python-Projects\Automate-The-Boring-Stuff-With-Python\spam.png')
debugVar_ExistsTrue = os.path.exists('c:\Development\Python-Projects\Automate-The-Boring-Stuff-With-Python')

# Print Debug Variable
print(debugVar_ExistsFalse)
print(debugVar_ExistsTrue)

# Create a Debug Variable for os.path.isfile(), to return a Boolean value based upon whether or not the value passed resolves as a File
debugVar_IsFileFalse = os.path.isfile('C:\Development\Python-Projects\Automate-The-Boring-Stuff-With-Python\Section_11_Files\Lesson_30_FilenamesAbsoluteRelativePaths')
debugVar_IsFileTrue = os.path.isfile('C:\Development\Python-Projects\Automate-The-Boring-Stuff-With-Python\Section_11_Files\Lesson_30_FilenamesAbsoluteRelativePaths\lesson30-recap.txt')

# Print Debug Variable
print(debugVar_IsFileFalse)
print(debugVar_IsFileTrue)

# Create a Debug Variable for os.path.isdir(), to return a Boolean value based upon whether or not the value passed resolves as a Directory
debugVar_IsDirFalse = os.path.isdir('C:\Development\Python-Projects\Automate-The-Boring-Stuff-With-Python\Section_11_Files\Lesson_30_FilenamesAbsoluteRelativePaths')
debugVar_IsDirTrue = os.path.isdir('C:\Development\Python-Projects\Automate-The-Boring-Stuff-With-Python\Section_11_Files\Lesson_30_FilenamesAbsoluteRelativePaths\lesson30-recap.txt')

# Print Debug Variable
print(debugVar_IsDirFalse)
print(debugVar_IsDirTrue)

# Create a Debug Variable for os.path.getsize(), to return a Bitsize value when the Path value passed resolves as a File
debugVar_GetSize = os.path.getsize('C:\Development\Python-Projects\Automate-The-Boring-Stuff-With-Python\Section_11_Files\Lesson_30_FilenamesAbsoluteRelativePaths\lesson30-recap.txt')

# Print Debug Variable
print(debugVar_GetSize)

# Create a Debug Variable for os.listdir(), to return a List of all Folders/Files found based upon the Path value passed
debugVar_ListDirFiles = os.listdir('C:\Development\Python-Projects\Automate-The-Boring-Stuff-With-Python\Section_11_Files\Lesson_30_FilenamesAbsoluteRelativePaths')
debugVar_ListDirFolders = os.listdir('C:\Development\Python-Projects\Automate-The-Boring-Stuff-With-Python\Section_11_Files')

# Print Debug Variable
print(debugVar_ListDirFiles)
print(debugVar_ListDirFolders)

# Create a Debug Variable for os.makedirs(), to create Directories at the based upon the Path value passed
debugVar_BeforeMakeDir = os.listdir('C:\Development\Python-Projects\Automate-The-Boring-Stuff-With-Python\Section_11_Files\Lesson_30_FilenamesAbsoluteRelativePaths')

# Print Debug Variable
print(debugVar_BeforeMakeDir)

# Create a Debug Variable for os.makedirs(), to create Directories at the based upon the Path value passed
os.makedirs('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_30_FilenamesAbsoluteRelativePaths\\delicious\\walnut\\waffles')


debugVar_AfterMakeDir = os.listdir('C:\Development\Python-Projects\Automate-The-Boring-Stuff-With-Python\Section_11_Files\Lesson_30_FilenamesAbsoluteRelativePaths')

# Print Debug Variable
print(debugVar_AfterMakeDir)

# Clean-up, delete the Directories recently made
os.removedirs('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_30_FilenamesAbsoluteRelativePaths\\delicious\\walnut\\waffles')
