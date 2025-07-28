# The regex method findall() is passed a string, and returns all matches in it, not just the first match.
# If the regex has 0 or 1 group, findall() returns a list of strings.
# If the regex has 2 or more groups, findall() returns a list of tuples of strings.
# \d is a shorthand character class that matches digits. \w matches "word characters" (letters, numbers, and the underscore). \s matches whitespace characters (space, tab, newline).
# The uppercase shorthand character classes \D, \W, and \S match charaters that are not digits, word characters, and whitespace.
# You can make your own character classes with square brackets: [aeiou]
# A ^ caret makes it a negative character class, matching anything not in the brackets: [^aeiou]

# import the Regex modole
import re

# Create a Regex Pattern Matching Object for Digit, Space, then words
xmasRegex = re.compile(r'\d+\s\w+')

# Create a String Variable based upon a sample Resume (https://www.linkedin.com/jobs/collections/recommended/?currentJobId=4262459768)
lyricsDaysOfChristmas = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans  a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 French hens, 2 turtle doves, and 1 partridge in a pear tree!'

# Utilize re.findall() to return a List of all the matches and create a variable to store the data
xmasValues = xmasRegex.findall(lyricsDaysOfChristmas)

# Print to screen the output
print(xmasValues)