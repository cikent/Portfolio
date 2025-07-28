# The sub() regex method will substitute matches with some other text.
# Using \1, \2 and so will substitute group 1, 2, etc in the regex pattern.
# Passing re.VERBOSE lets you add whitespace and comments to the regex string passed to re.compile().
# If you want to pass multiple arguments (re.DOTALL , re.IGNORECASE, re.VERBOSE), combine them with the | bitwise operator.

# Import the regex module
import re

# Create a Regex Search Pattern based upon Agent Names
namesRegex = re.compile(r'Agent (\w)\w*')

# Create a Variable and store the Search results inside
beforeSubResult = namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')

# Print to the screen the results before substitutions
print(beforeSubResult)

# Utilize the Sub method to find and replace (i.e. substitute) a new value
afterSubResult = namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.')

# Print to the screen the results after substitutions
print(afterSubResult)