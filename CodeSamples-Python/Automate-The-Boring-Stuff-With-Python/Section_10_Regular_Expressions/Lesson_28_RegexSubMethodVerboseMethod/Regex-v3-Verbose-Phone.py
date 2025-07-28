# The sub() regex method will substitute matches with some other text.
# Using \1, \2 and so will substitute group 1, 2, etc in the regex pattern.
# Passing re.VERBOSE lets you add whitespace and comments to the regex string passed to re.compile().
# If you want to pass multiple arguments (re.DOTALL , re.IGNORECASE, re.VERBOSE), combine them with the | bitwise operator.

# Import the regex module
import re

# Create a Regex Search Pattern based upon Agent Names
verbosePhoneRegex = re.compile(r'''
(\d\d\d)|       # area code (without parens)
(\(\d\d\d\) )   # -or- area code with parens and no dash
\d\d\d          # first 3 digits
-               # second dash
\d\d\d\d        # last 4 digits
\sx\d{2,4}      # extension, like x1234''', re.IGNORECASE | re.DOTALL | re.VERBOSE)     # Include multiple arguments with a bitwise OR operation (i.e. the | character)

# Utilize the regex expression findall() to return a List of all Strings matching the defined regex pattern
phoneVar = verbosePhoneRegex.findall('Call me at 415-555-1011 tomorrow, or at 415-555-9999 for my office line.')

# Print to the screen the results before substitutions
print(phoneVar)