# ^ means the string must start with pattern, $ means the string must end with the pattern. Both means the entire string must match the entire pattern.
# The . dot is a wildcard; it matches any character except newlines.
# Pass re.DOTALL as the second argument to re.compile() to make the . dot match newlines as well.
# Pass re.I as the second argument to re.compile() to make the matching case-insensitive.

# import the Regex modole
import re

# Create a Dot Star Sign Character Class to find anything that matches the pattern
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')

# Create a String Variable to contain sample text
samepleText1 = 'First Name: Christopher Last Name: Kent'

# Utilize re.findall() to return a List of all the matches and create a variable to store the data
dotStarReturnValue = nameRegex.findall(samepleText1)

# Print to screen the output of the Regex expressions
print(dotStarReturnValue)
