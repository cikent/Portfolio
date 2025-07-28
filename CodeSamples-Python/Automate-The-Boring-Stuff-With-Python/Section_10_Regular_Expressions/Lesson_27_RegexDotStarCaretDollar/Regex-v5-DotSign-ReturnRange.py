# ^ means the string must start with pattern, $ means the string must end with the pattern. Both means the entire string must match the entire pattern.
# The . dot is a wildcard; it matches any character except newlines.
# Pass re.DOTALL as the second argument to re.compile() to make the . dot match newlines as well.
# Pass re.I as the second argument to re.compile() to make the matching case-insensitive.

# import the Regex modole
import re

# Create a Dot Sign Character Class to find anything that matches the pattern combined with a Range prefacing the value
atRegex = re.compile(r'.{1,2}at')

# Utilize re.findall() to return a List of all the matches and create a variable to store the data
dotWildcardReturnValue = atRegex.findall('The cat in the hat sat on the flat mat.')

# Print to screen the output of the Regex expressions
print(dotWildcardReturnValue)           # Notice all values returned are 4 Characters long because .at is 3 combined with the Range of 2. These results can include White Space characters.
