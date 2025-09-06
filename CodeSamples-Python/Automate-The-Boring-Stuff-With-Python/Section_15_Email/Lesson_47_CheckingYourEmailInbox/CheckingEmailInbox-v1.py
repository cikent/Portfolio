# Import relevant modules
import imapclient, datetime, pyzmail

# Create Script Variables
YOUR_GOOGLE_EMAIL = 'ckentautobot@gmail.com'  # The dummy email I've setup to test sending an email via STMP using an app password
YOUR_GOOGLE_EMAIL_FAKE_APP_PASSWORD = 'abcd efgh ijkl mnop'  # Fake app password I've generated

# Create a Connection Object; 1st Argument == Email Provider Server, 2nd Argument == Encryption Keyword value
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)

# Login to the Email Server; 1st Argument = Email Alias, 2nd Argument = Credentials
conn.login(YOUR_GOOGLE_EMAIL, YOUR_GOOGLE_EMAIL_FAKE_APP_PASSWORD)         # Fake App Password

# Select the desired Email Server Folder; 1st Arguement == Email Server Folder name, 2nd Argument == readonly=True (to avoid deleting Emails)
conn.select_folder('INBOX', readonly=True)

# Search the Selected Folder for XYZ; Utilize new IMAPClient Class search() method syntax by passing in datetime.date()
UIDS = conn.search([u'SINCE', datetime.date(2025,9,2)])

# Print Debug
print(UIDS)

# Translate the Email Unique IDs from Integers into useful data utilizing the fetch() method;  
# rawMessageEmail1 = conn.fetch([3], ['BODY[]', 'FLAGS'])             # Retrieve the UIDs message, data and any modifiers
# rawMessageEmail2 = conn.fetch([4], ['BODY[]', 'FLAGS'])             # Retrieve the UIDs message, data and any modifiers
rawMessageEmail3 = conn.fetch([5], ['BODY[]', 'FLAGS'])             # Retrieve the UIDs message, data and any modifiers

# Print Debug
# print(rawMessageEmail1)
# print(rawMessageEmail2)
print(rawMessageEmail3)

# Utilize Pyzmail to parse the Raw Email Message text to create a PyzMessage Object
# pyzMessageEmail1 = pyzmail.PyzMessage.factory(rawMessageEmail1[3][b'BODY[]'])
# pyzMessageEmail2 = pyzmail.PyzMessage.factory(rawMessageEmail2[4][b'BODY[]'])
pyzMessageEmail3 = pyzmail.PyzMessage.factory(rawMessageEmail3[5][b'BODY[]'])

# Print Debug
# print(pyzMessageEmail1)
# print(pyzMessageEmail2)
print(pyzMessageEmail3)

# # Print the pyzMessage1 various properties
# print(pyzMessageEmail1.get_subject())                   # Print the pyzMessage.get_subject Property
# print(pyzMessageEmail1.get_addresses('from'))           # Print the pyzMessage.get_addresses Property
# print(pyzMessageEmail1.get_addresses('to'))             # Print the pyzMessage.get_addresses Property
# print(pyzMessageEmail1.get_addresses('bcc'))            # Print the pyzMessage.get_addresses Property
# print(pyzMessageEmail1.text_part)                       # Print the pyzMessage.text_part Property
# print(pyzMessageEmail1.text_part.get_payload().decode('UTF-8'))                       # Print the pyzMessage.text_part Property

# # Print the pyzMessage2 various properties
# print(pyzMessageEmail2.get_subject())                   # Print the pyzMessage.get_subject Property
# print(pyzMessageEmail2.get_addresses('from'))           # Print the pyzMessage.get_addresses Property
# print(pyzMessageEmail2.get_addresses('to'))             # Print the pyzMessage.get_addresses Property
# print(pyzMessageEmail2.get_addresses('bcc'))            # Print the pyzMessage.get_addresses Property
# print(pyzMessageEmail2.text_part)                       # Print the pyzMessage.text_part Property
# print(pyzMessageEmail2.text_part.get_payload().decode('UTF-8'))                       # Print the pyzMessage.text_part Property

# Print the pyzMessage3 various properties
print(pyzMessageEmail3.get_subject())                   # Print the pyzMessage.get_subject Property
print(pyzMessageEmail3.get_addresses('from'))           # Print the pyzMessage.get_addresses Property
print(pyzMessageEmail3.get_addresses('to'))             # Print the pyzMessage.get_addresses Property
print(pyzMessageEmail3.get_addresses('bcc'))            # Print the pyzMessage.get_addresses Property
print(pyzMessageEmail3.text_part)                       # Print the pyzMessage.text_part Property
print(pyzMessageEmail3.text_part.get_payload().decode('UTF-8'))                       # Print the pyzMessage.text_part Property

# Find all the Folders associated to the Connection
connFolders = conn.list_folders()

# Print Debug
print(connFolders)

# Select the desired Email Server Folder; 1st Arguement == Email Server Folder name, 2nd Argument == readonly=False (to allow deleting Emails)
conn.select_folder('INBOX', readonly=False)

# Search the Selected Folder for XYZ; Utilize new IMAPClient Class search() method syntax by passing in datetime.date()
UIDSBeforeDelete = conn.search([u'SINCE', datetime.date(2025,9,2)])

# Print Debug
print(UIDSBeforeDelete)

# Delete Email Messages
conn.delete_messages([4])

# Search the Selected Folder for XYZ; Utilize new IMAPClient Class search() method syntax by passing in datetime.date()
UIDSAfterDelete = conn.search([u'SINCE', datetime.date(2025,9,2)])

# Print Debug
print(UIDSAfterDelete)

# Close the connection
conn.logout()