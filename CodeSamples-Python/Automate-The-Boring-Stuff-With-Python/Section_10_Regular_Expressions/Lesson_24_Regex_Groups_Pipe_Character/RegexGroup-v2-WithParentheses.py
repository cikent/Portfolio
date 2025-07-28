# Groups are created in regex strings with parentheses.
# The first set of parentheses is group 1, the second is 2, and so on.
# Calling group() or group(0) returns the full matching string, group(1) returns group 1's matching string, and so on.
# Use \( and \) to match literal parentheses in the regex string.
# The | pipe can match one of many possible groups.

# import the regex module
import re

# Create a regex String object based upon a phone number value we want to identify WITH groups
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')

# Declare String Variable containing a Phone Number WITH ()'s
exampleStringWithParentheses = 'My phone number is (415) 555-4242'

# Utilize the regex expression search method to create a new Match Object variable IF a pattern match is found
matchObject1 = phoneNumRegex.search(exampleStringWithParentheses)

# Print to screen the Regex Match Object Group values, then entire Group, and each distinct index value
print('Print to screen the Regex Match Object Group values. 1st: the entire Group, then each distinct index value:', end='\n')
print('The mo.object() value is: ' + matchObject1.group())
print('The mo.object(1) value is: ' + matchObject1.group(1))
print('The mo.object(2) value is: ' + matchObject1.group(2))
