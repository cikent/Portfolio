# ^ means the string must start with pattern, $ means the string must end with the pattern. Both means the entire string must match the entire pattern.
# The . dot is a wildcard; it matches any character except newlines.
# Pass re.DOTALL as the second argument to re.compile() to make the . dot match newlines as well.
# Pass re.I as the second argument to re.compile() to make the matching case-insensitive.

# import the Regex modole
import re

# Create a String Variable to contain sample text
sampleText1 = 'Al, why does your programming book talk about RoboCop so much?'

# Create a Custom Character Class to find vowels: aeiou does NOT include Casing
vowelNoCasingRegex = re.compile(r'[aeiou]')

# Create a Custom Character Class to find vowels using the Ignore casing argument
# vowelCasingRegex = re.compile(r'[aeiou]', re.I)
vowelCasingRegex = re.compile(r'[aeiou]', re.IGNORECASE)

# Utilize re.findall() to return a List of all the matches and create a variable to store the data
vowelNoCasing = vowelNoCasingRegex.findall(sampleText1)

# Utilize re.findall() to return a List of all the matches and create a variable to store the data
vowelCasing = vowelCasingRegex.findall(sampleText1)

# Print to screen the output of the Regex expressions
print(vowelNoCasing)
print(vowelCasing)