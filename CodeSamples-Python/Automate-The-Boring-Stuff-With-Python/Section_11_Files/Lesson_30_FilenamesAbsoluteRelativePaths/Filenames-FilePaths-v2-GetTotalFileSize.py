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

# Create an Integer variable
totalSize = 0

# Create a Program to determine the Size of a Directory value passed
for filename in os.listdir('c:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python'):
    if not os.path.isfile(os.path.join('c:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('c:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python', filename))

# Print Debug Variable
print(totalSize)