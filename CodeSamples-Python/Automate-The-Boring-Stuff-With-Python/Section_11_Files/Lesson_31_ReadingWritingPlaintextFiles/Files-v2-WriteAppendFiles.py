# The open() function will return a file object which has reading and writing –related methods.
# Pass ‘r' (or nothing) to open() to open the file in read mode. Pass ‘w' for write mode. Pass ‘a' for append mode.
# Opening a nonexistent filename in write or append mode will create that file.
# Call read() or write() to read the contents of a file or write a string to a file.
# Call readlines() to return a list of strings of the file's content.
# Call close() when you are done with the file.
# The shelve module can store Python values in a binary file.
# The shelve.open() function returns a dictionary-like shelf value.

# Create a File Object using the open() method using a Path value as the 1st argument, pass 'w' as the 2nd argument to Write to the file
helloFile = open('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_31_ReadingWritingPlaintextFiles\\Hello2.txt', 'w')

# Write to Hello2.txt multiple times
helloFile.write('Hello!!!!!!!!')       # 1st time
helloFile.write('Hello!!!!!!!!')       # 2nd time
helloFile.write('Hello!!!!!!!!')       # 3rd time

# Create a File Object using the open() method using a Path value as the 1st argument, pass 'a' as the 2nd argument to Append to the file
helloFile3 = open('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_11_Files\\Lesson_31_ReadingWritingPlaintextFiles\\Hello2.txt', 'a')

# Append to Hello2.txt multiple times
helloFile.write('\nHello!!!!!!!!')       # 1st time
helloFile.write('\nHello!!!!!!!!')       # 2nd time
helloFile.write('\nHello!!!!!!!!')       # 3rd time

# Close the File Object
helloFile.close()
