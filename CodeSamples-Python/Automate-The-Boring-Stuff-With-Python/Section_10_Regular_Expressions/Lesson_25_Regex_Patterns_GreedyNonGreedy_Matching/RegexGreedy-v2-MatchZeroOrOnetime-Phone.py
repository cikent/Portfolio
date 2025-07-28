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
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')

# Search the 1st Match Object for the Regex Expression String
mo1 = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')

# Search the 2nd Match Object for the Regex Expression String
mo2 = phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')

# Print to screen the 1st Regex Match Object value mo1 found within the Regex String Object
print('Print to screen the 1st Regex Match Object value mo1 found within the Regex String Object:', end='\n')
print(str(mo1))
print(mo1.group())

# Print to screen the 2nd Regex Match Object value mo2 found within the Regex String Object
print('Print to screen the 2nd Regex Match Object value mo2 found within the Regex String Object:', end='\n')
print(str(mo2))
print(mo2.group())

