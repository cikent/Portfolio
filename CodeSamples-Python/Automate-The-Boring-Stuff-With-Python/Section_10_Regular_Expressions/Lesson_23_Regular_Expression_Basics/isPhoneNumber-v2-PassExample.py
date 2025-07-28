# Utilize the Function to verify whether or not a  Users supplied String Argument does indeed contain a valid Phone Number.
# - Example message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9999 for my office line.'
# GIVEN the User passes a valid String Argument to the defined Function
#     WHEN the value has a valid USA OR Canada Phone Number 
#         THEN print to UI the Phone number found
#     WHEN the value is NOT a valid USA OR Canada Phone Number 
#         THEN print to UI no phone numbers were found

def isPhoneNumber(text):  # 415-555-1234
    if len(text) != 12:
        return False # not phone number-sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False # missing first dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False # no first 3 digits
    if text[7] != '-':
        return False # missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False # missing last 4 digits
    return True

""" print(isPhoneNumber('hello'))           # False example
print(isPhoneNumber('4155551234'))      # False example
print(isPhoneNumber('abc-def-hijk'))    # False example
print(isPhoneNumber('415-555-1234'))    # True example """

# Parse a String Message to determine if it contains valid Phone numbers within
message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9999 for my office line.'

# Declare Boolean variable to indicate whether or NOT a PhoneNumber was identified in the passed Argument for the Functions Parameter
foundNumber = False

for i in range(len(message)):
  chunk = message[i:i+12]
  if isPhoneNumber(chunk):
          print('Phone number found: ' + chunk)
          foundNumber = True        # Set the boolean variable to True IF a valid Phone number is detected in the string
if not foundNumber:
    print('Could not find any phone numbers')
    
""" print('Done') """
