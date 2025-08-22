# The Requests module is a third-party module for downloading web pages and files.
# requests.get() returns a Response object.
# The raise_for_status() Response method will raise an exception if the download failed.
# You can save a downloaded file to your hard drive with calls to the iter_content() method.

# Import relevant modules
import requests

# Utilize requests.get() to download a file by passing a valid URL as the arguement and store the value in a Response Object
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# Bad Request Example
badRes = requests.get('https://automatetheboringstuff.com/asdflkj123456')

# Verify the the Response Object's Raise Status Value
responseBadRaiseStatusValue = badRes.raise_for_status

# Print Debug output
print(responseBadRaiseStatusValue)