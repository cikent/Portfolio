"""
Utilize Regular Expressions to simply the overall code.
Regular expressions are mini-lanugague for specifying text patterns. Writing code to do pattern matching without regular expressions is a huge pain.
- Regex strings often use backslashes (like \d), so they are often raw strings: r'\d'
- Import the re module first
- Call the re.compile() function to create a regex object.
- Call the regex object's search() method to create a match object.
- Call the match object's group() method to get the matchd string.
- \d is the regex for a numeric digit character.
"""

# Import the re Module, which contains: All the regex functions in Python are in the re module.
import re

# Declare String Variable
message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9999 for my office line.'

# Declare a variable representing the text pattern we're searching for (i.e. a phone number)
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Utilize the regex expression search method to create a new Match Object variable IF a pattern match is found
mo = phoneNumRegex.search(message)

# Print to UI the 1st occurrence of any Match Objects variables found
print(mo.group())