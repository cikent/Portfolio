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
batRegex = re.compile(r'Bat(wo)*man')

# Search the 1st Match Object for the Regex Expression String
mo1 = batRegex.search('The Adventures of Batman')

# Search the 2nd Match Object for the Regex Expression String
mo2 = batRegex.search('The Adventures of Batwoman')

# Search the 3rd Match Object for the Regex Expression String which will return NONE because no match exists
mo3 = batRegex.search('The Adventures of Batwowowowoman')

# Print to screen the 1st Regex Match Object value mo1 found within the Regex String Object
print('Print to screen the 1st Regex Match Object value mo1 found within the Regex String Object:', end='\n')
print(str(mo1))
print(mo1.group())

# Print to screen the 2nd Regex Match Object value mo2 found within the Regex String Object
print('Print to screen the 2nd Regex Match Object value mo2 found within the Regex String Object:', end='\n')
print(str(mo2))
print(mo2.group())

# Print to screen the 3rd Regex Match Object value mo3 found within the Regex String Object
print('Print to screen the 3rd Regex Match Object value mo3 found within the Regex String Object:', end='\n')
print(str(mo3))
print(mo3.group())