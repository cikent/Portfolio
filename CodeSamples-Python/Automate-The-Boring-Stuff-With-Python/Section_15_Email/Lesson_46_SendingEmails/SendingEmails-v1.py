# Import relevant modules
import smtplib, os

# Create Script Variables
YOUR_GOOGLE_EMAIL = 'ckentautobot@gmail.com'  # The dummy email I've setup to test sending an email via STMP using an app password
YOUR_GOOGLE_EMAIL_FAKE_APP_PASSWORD = 'abcd efgh ijkl mnop'  # Fake app password I've generated

# Create a Connection Object; 1st Argument = Host String Domain Name, 2nd Argument = Port Number
conn = smtplib.SMTP('smtp.gmail.com', 587)

# Connect to the Server (i.e. Send internet traffic from the Python Program)
conn.ehlo()

# Start TLS Encryption to ensure Password is can be passed
conn.starttls()

# Login to the Email Server; 1st Argument = Email Alias, 2nd Argument = Credentials
# conn.login(YOUR_GOOGLE_EMAIL, YOUR_GOOGLE_EMAIL_FAKE_APP_PASSWORD)         # Fake App Password

# Send a Test Email; 1st Argument = Sending Email Alias, 2nd Argument = Receiving Email Alias, 3rd Argument = Subject & Body
sentFrom = YOUR_GOOGLE_EMAIL
sentTo = sentFrom  #  Send it to self (as test)
emailSubjectBody = 'Subject: So long... \n\nDear Chris, \nSo long, and thanks for all the fish.'
# conn.sendmail(sentFrom, sentTo, emailSubjectBody)

# Close the connection
conn.quit()

# Update Working Directory to Local Lesson Folder where the example.xlsx file resides
os.chdir('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_15_Email\\Lesson_46_SendingEmails')

# Verify the Current Working Directory
filePath = os.getcwd()

# DEBUG Print the Current Working Directories File Path
# print(filePath)

# Print Verification Evidence
print('Assume the Commented Out Code is enabled with a valid App Password provided... \nFor evidence, via Github, see the "SendEmail-Via-SMTP-Proof.jpg" file @ https://github.com/cikent/Python-Projects/blob/master/Automate-The-Boring-Stuff-With-Python/Section_15_Email/Lesson_46_SendingEmails/SendEmail-Via-SMTP-Proof.jpg')