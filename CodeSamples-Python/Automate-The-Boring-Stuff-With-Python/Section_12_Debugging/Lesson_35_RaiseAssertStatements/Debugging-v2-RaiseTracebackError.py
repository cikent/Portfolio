# You can raise your own exceptions: raise Exception(‘This is the error message.')
# You can also use assertions: assert condition, ‘Error message'
# Assertions are for detecting programmer errors that are not meant to be recovered from. User errors should raise exceptions.

# Import relelvant Modules
import traceback

# IF an Error is caused, this Block will execute:
# TODO: # os.chdir() will change the current working directory.
try:
    # This is the String that will be generated in the File
    raise Exception('This is the Traceback Error message!')
except:
    # Utilize open() to create a File and Append in the Current Working Directory (C:\Development\Python-Projects\Automate-The-Boring-Stuff-With-Python)
    errorFile = open('error_log.txt', 'a')
    # Write the Traceback Stack that caused the Error
    errorFile.write(traceback.format_exc())
    # Close the File Object
    errorFile.close()
    # Print to Output that the file was written to
    print('The traceback info was written to error_log.txt')

# Programmatically create this Example Text Output
"""

*************
*           *
*           *
*           *
*************

"""

# Create a function that will create an example of the pattern above
def boxPrint(Symbol, Width, Height):
    # 1st Exception: Ensure Symbol is 1 String length long
    if len(Symbol) != 1:
        raise Exception('Raise Exception Error: The "Symbol" value MUST be a String length EQUAL TO 1.')
    # 2nd Exception: Ensure Width and Height are 2 or higher
    if (Width < 2) or (Height < 2):
        raise Exception('Raise Exception Error: The "Width" and "Height" argument values MUST be GREATER THAN or EQUAL TO 2.')
    
    # Print the 1st Row based upon the Symbol and Width provided
    print(Symbol * Width)

    # Print this pattern based upon the Height value; Minus 2 for the Top and Bottom Rows
    for i in range(Height - 2):
        # Print the symbol, add the # of spaces based upon Width minus border, then print symbol again
        print(Symbol + (' ' * (Width - 2)) + Symbol)

    # Print the 2nd Row based upon the Symbol and Width provided
    print(Symbol * Width)

# Print Example output of function
# boxPrint('*', 15, 5)        # 1st Example, desired output
# boxPrint('O', 5, 16)        # 2nd Example, desired output
boxPrint('**', 15, 5)       # 3rd Example, NOT desired output, create 1st Exception
# boxPrint('*', 1, 1)         # 3rd Example, NOT desired output, create 2nd Exception
                