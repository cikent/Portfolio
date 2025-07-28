# Groups are created in regex strings with parentheses.
# The first set of parentheses is group 1, the second is 2, and so on.
# Calling group() or group(0) returns the full matching string, group(1) returns group 1's matching string, and so on.
# Use \( and \) to match literal parentheses in the regex string.
# The | pipe can match one of many possible groups.

# import the regex module
import re

# Declare a regex variable representing the text pattern we're searching for delimited by | pipes
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

# Declare String Variable containing a multiple Bat references
exampleStringWithBatReferences = 'Batman\'s Batmobile lost a wheel when it dropped from his Batcopter at Batbat o\'clock at night!'

# Create a Match Object Tuple List based upon all batRegex values identified
batRegexList = batRegex.findall(exampleStringWithBatReferences)

# Print to screen the Regex Match Object Group values, then entire Group, and each distinct index value
print('Print to screen the Regex String varianble utilized to search against for Match Object Group values: ', end='\n')
print(str(exampleStringWithBatReferences), end='\n')
print('Print to screen the Regex Match Object Group values. Any references from the string that include \'Bat\':', end='\n')
print('The mo.object() value is: ' + str(batRegexList))