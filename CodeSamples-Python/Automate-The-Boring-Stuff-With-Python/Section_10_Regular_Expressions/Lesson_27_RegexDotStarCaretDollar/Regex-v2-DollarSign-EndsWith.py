# ^ means the string must start with pattern, $ means the string must end with the pattern. Both means the entire string must match the entire pattern.
# The . dot is a wildcard; it matches any character except newlines.
# Pass re.DOTALL as the second argument to re.compile() to make the . dot match newlines as well.
# Pass re.I as the second argument to re.compile() to make the matching case-insensitive.

# import the Regex modole
import re

# Create a Dollar Sign Character Class to find a specific value at the End of a String
endsWithWorldRegex = re.compile(r'world!$')

# Utilize re.search() to return a List of all the matches and create a variable to store the data
dollarSignReturnValue = endsWithWorldRegex.search('Hello world!')
dollarSignNoReturnValue = endsWithWorldRegex.search('Hello world!asfdasdfasdf')

# Print to screen the output of the Regex expressions
print(dollarSignReturnValue)
print(dollarSignNoReturnValue)