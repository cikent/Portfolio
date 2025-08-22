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

# Verify the the Response Object's Raise Status Value
responseRaiseStatusValue = res.raise_for_status

# Print Debug output
print(responseRaiseStatusValue)

# Print the 1st 500 Characters from the Response Object's Text
print(res.text[:500])
