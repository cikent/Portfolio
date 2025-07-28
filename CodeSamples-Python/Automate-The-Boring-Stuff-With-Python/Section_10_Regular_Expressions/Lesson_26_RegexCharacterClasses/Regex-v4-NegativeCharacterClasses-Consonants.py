# The regex method findall() is passed a string, and returns all matches in it, not just the first match.
# If the regex has 0 or 1 group, findall() returns a list of strings.
# If the regex has 2 or more groups, findall() returns a list of tuples of strings.
# \d is a shorthand character class that matches digits. \w matches "word characters" (letters, numbers, and the underscore). \s matches whitespace characters (space, tab, newline).
# The uppercase shorthand character classes \D, \W, and \S match charaters that are not digits, word characters, and whitespace.
# You can make your own character classes with square brackets: [aeiou]
# A ^ caret makes it a negative character class, matching anything not in the brackets: [^aeiou]

# import the Regex modole
import re

# Create a Negative Character Class to find Consonants (i.e. NOT vowels: aeiouAEIOU)
consonantsRegex = re.compile(r'[^aeiouAEIOU]')

# Utilize re.findall() to return a List of all the matches and create a variable to store the data
consonantsValues = consonantsRegex.findall('Robocop eats baby food.')

# Print to screen the output of the Regex expressions
print(consonantsValues)