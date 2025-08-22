# The open() function will return a file object which has reading and writing –related methods.
# Pass ‘r' (or nothing) to open() to open the file in read mode. Pass ‘w' for write mode. Pass ‘a' for append mode.
# Opening a nonexistent filename in write or append mode will create that file.
# Call read() or write() to read the contents of a file or write a string to a file.
# Call readlines() to return a list of strings of the file's content.
# Call close() when you are done with the file.
# The shelve module can store Python values in a binary file.
# The shelve.open() function returns a dictionary-like shelf value.

# Create a File Object using the open() method using a Path value as the 1st argument
helloFile = open('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_31_ReadingWritingPlaintextFiles\\Hello.txt')

# Utilize the File Object read() method to return a single String based upon the File Object
readContents = helloFile.read()

# Utilize the File Object readlines() method to return a List of String based upon the File Object
readLinesContents = helloFile.readlines()

# Print to screen the variable
print(readContents)
print(readLinesContents)

# Close the File Object
helloFile.close()
