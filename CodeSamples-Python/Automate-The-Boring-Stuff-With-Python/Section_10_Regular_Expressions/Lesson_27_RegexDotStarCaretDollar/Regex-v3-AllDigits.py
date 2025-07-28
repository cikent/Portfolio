# ^ means the string must start with pattern, $ means the string must end with the pattern. Both means the entire string must match the entire pattern.
# The . dot is a wildcard; it matches any character except newlines.
# Pass re.DOTALL as the second argument to re.compile() to make the . dot match newlines as well.
# Pass re.I as the second argument to re.compile() to make the matching case-insensitive.

# import the Regex modole
import re

# Create a All Digit Character Class to verify a String contains only numeric characters
allDigitsRegex = re.compile(r'^\d+$')

# Utilize re.search() to return a List of all the matches and create a variable to store the data
allDigitsReturnValue = allDigitsRegex.search('1234567890')
allDigitsNoReturnValue = allDigitsRegex.search('12345x67890')

# Print to screen the output of the Regex expressions
print(allDigitsReturnValue)
print(allDigitsNoReturnValue)