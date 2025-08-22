# The open() function will return a file object which has reading and writing –related methods.
# Pass ‘r' (or nothing) to open() to open the file in read mode. Pass ‘w' for write mode. Pass ‘a' for append mode.
# Opening a nonexistent filename in write or append mode will create that file.
# Call read() or write() to read the contents of a file or write a string to a file.
# Call readlines() to return a list of strings of the file's content.
# Call close() when you are done with the file.
# The shelve module can store Python values in a binary file.
# The shelve.open() function returns a dictionary-like shelf value.

# Import relevant modules
import os, shelve

# Change the working directory
os.chdir('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_31_ReadingWritingPlaintextFiles')

# Create a Binary Shelf File Object using the open() method via the local Current Working Directory
shelfFile = shelve.open('mydata')

# Create a List variable based upon my Cats
shelfFile['cats'] = ['Bones', 'Gunner', 'Dina', 'Briar']

# Close the File Object
shelfFile.close()

# Open the Shelved File Object
shelfFile = shelve.open('mydata')

# Create a variable to save the Shelf File Object Keys View Value
myCatsBinaryShelfKeysViewValue = shelfFile.keys()

# Create a variable to save the Shelf File Object Keys View Keys Value
myCatsShelfKeysViewKeysValue = list(shelfFile.keys())

# Create a variable to save the Shelf File Object View Keys Values Value
myCatsShelfViewValuesValue = list(shelfFile.values())

# Print Debug Variable
print(myCatsBinaryShelfKeysViewValue)
print(myCatsShelfKeysViewKeysValue)
print(myCatsShelfViewValuesValue)
