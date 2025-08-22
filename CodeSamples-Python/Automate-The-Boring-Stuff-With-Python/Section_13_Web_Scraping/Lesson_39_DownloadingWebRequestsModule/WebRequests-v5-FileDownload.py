# The Requests module is a third-party module for downloading web pages and files.
# requests.get() returns a Response object.
# The raise_for_status() Response method will raise an exception if the download failed.
# You can save a downloaded file to your hard drive with calls to the iter_content() method.

# Import relevant modules
import requests

# Utilize requests.get() to download a file by passing a valid URL as the arguement and store the value in a Response Object
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# Verify the the Response Object's Status Code value
responseStatusCodeValue = res.status_code

# Print Debug output
print(responseStatusCodeValue)

# # Verify the the Response Object's Raise Status Value
# responseRaiseStatusValue = res.raise_for_status

# # Print Debug output
# print(responseRaiseStatusValue)

# # Print the 1st 500 Characters from the Response Object's Text
# print(res.text[:500])

# # Bad Request Example
# badRes = requests.get('https://automatetheboringstuff.com/asdflkj123456')

# # Verify the the Response Object's Raise Status Value
# responseBadRaiseStatusValue = badRes.raise_for_status

# # Print Debug output
# print(responseBadRaiseStatusValue)

# Save the Request Response to a Local File Object, wb == write binary
playFile = open('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_13_Web_Scraping\\Lesson_39_DownloadingWebRequestsModule\\RomeoAndJuliet.txt', 'wb')

# Loop through writes of the file
for chunk in res.iter_content(100000):
    playFile.write(chunk)

# Close the File Object
playFile.close()