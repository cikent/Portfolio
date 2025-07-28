#! python3

# Source 1 PDF File location: https://2009-2017.state.gov/documents/organization/112065.pdf
# Source 2 PDF File location: https://www.asusystem.edu/staff/directory/
# Create a Program to Search a PDF for all the viable Phone and Email values

# import relevant modules
import re, pyperclip

# Create a Regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, x12345

(
((\d\d\d) | (\(\d\d\d\)))?             # area code (optional)
(\s|-)                                 # first seperator
\d\d\d                                 # first 3 digits
-                                      # second seperator
\d\d\d\d                               # last 4 digits
(((ext(\.)?\s) |x)                     # extension word-part (optional)
 (\d{2,5}))?                           # extension number-part (optional)
)
''', re.VERBOSE)

# Create a Regex for email addressess
emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5}))?.com
                        
[a-zA-Z0-9_.+]+                     # name part
@                                   # @ symbol
[a-zA-Z0-9_.+]+                     # domain part         
                        ''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()            # Save the Clipboard Text in a String Variable

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

# Create an empty List to contain all the extracted Phone Numbers
allPhoneNumbers = []        

# Increment through all the extracted Phone Number data and save the 1st String from the extractedPhone Tuple     
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])          # Save the 1st String from the extractedPhone Tuple    

# Debug Print
# print(allPhoneNumbers)
# print(extractedEmail)

# Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
