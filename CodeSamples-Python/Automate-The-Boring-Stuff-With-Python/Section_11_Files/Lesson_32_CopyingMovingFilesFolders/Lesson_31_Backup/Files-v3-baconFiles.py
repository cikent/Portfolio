# The open() function will return a file object which has reading and writing –related methods.
# Pass ‘r' (or nothing) to open() to open the file in read mode. Pass ‘w' for write mode. Pass ‘a' for append mode.
# Opening a nonexistent filename in write or append mode will create that file.
# Call read() or write() to read the contents of a file or write a string to a file.
# Call readlines() to return a list of strings of the file's content.
# Call close() when you are done with the file.
# The shelve module can store Python values in a binary file.
# The shelve.open() function returns a dictionary-like shelf value.

# Import relevant modules
import os

# Create a File Object using the open() method using a Path value as the 1st argument, pass 'w' as the 2nd argument to Write to the file
baconFile = open('bacon.txt', 'w')

# Write to bacon.txt
baconFile.write('Bacon is not a vegtable!')

# Create a File Object using the open() method using a Path value as the 1st argument, pass 'a' as the 2nd argument to Append to the file
baconFile = open('bacon.txt', 'a')

# Write to bacon.txt
baconFile.write('\n\nBacon is delicious!')

# Close the File Object
baconFile.close()

# Create a Debug Variable for os.getcwd(), to return the Current Working Directory
debugVar_OSGetCwd = os.getcwd()

# Print Debug Variable
print(debugVar_OSGetCwd)

# Verify the bacon file was created in the local Current Working Directory, because a relative path was passed instead of an absolute path when open() was called
debugVar_AfterWrite = os.listdir('C:\Development\Python-Projects\Automate-The-Boring-Stuff-With-Python')

# Print Debug Variable
print(debugVar_AfterWrite)

# Clean-up, delete the Bacon File recently made
os.remove('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\bacon.txt')         # Comment out to leave the bacon file created