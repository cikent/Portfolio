# The ? says the group matches zero or one times.
# The * says the group matches zero or more times.
# The + says the group matches one or more times.
# The curly braces can match a specific number of times.
# The curly braces with two numbers matches a minimum and maximum number of times.
# Leaving out the first or second number in the curly braces says there is no minimum or maximum.
# "Greedy matching" matches the longest string possible, "nongreedy matching" (or "lazy matching") matches the shortest string possible.
# Putting a question mark after the curly braces makes it do a nongreedy/lazy match.

# Import the Regex Module
import re

# Create a Regex Expression Object
phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')

# Search the 1st Match Object for the Regex Expression String
mo1 = phoneRegex.search('My numbers are 415-555-1234,555-4242,212-555-0000')

# Print to screen the 1st Regex Match Object value mo1 found within the Regex String Object
print('Print to screen the 1st Regex Match Object value mo1 found within the Regex String Object:', end='\n')
print('My numbers are 415-555-1234,555-4242,212-555-0000')
print(str(mo1))
print(mo1.group())