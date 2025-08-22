# The logging module lets you display logging messages.
# Log messages create a "breadcrumb trail" of what your program is doing.
# After calling logging.basicConfig() to set up logging, call logging.debug(‘This is the message') to create a log message.
# When done, you can disable the log messages with logging.disable(logging.CRITICAL)
# Don't use print() for log messages: It's hard to remove the mall when you're done debugging.
# The five log levels are: DEBUG, INFO, WARNING, ERROR, and CRITICAL.
# You can also log to a file instead of the screen with the filename keyword argument in the logging.basicConfig() function.

# Import relevant modules
import logging

# Create the basic Logging Setup
# Utilize filename= to create a File WITH a Relative File Path or Absolute File Path
logging.basicConfig(filename='C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_12_Debugging\\Lesson_36_Logging\\myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Disable the Logging at the CRITICAL level or lower
# logging.disable(logging.CRITICAL)

# Create Debug Log Messages:
logging.debug('Start of program')

# Create a function to calculate factorials
def factorial(n):
    # Create Debug Log Messages:
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    # Ensure the Range increment starts are 1, NOT 0
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s' % (total))
    return total

# Print to screen the results from running the factorial() function
print(factorial(5))

# Create Debug Log Messages:
logging.debug('End of program')