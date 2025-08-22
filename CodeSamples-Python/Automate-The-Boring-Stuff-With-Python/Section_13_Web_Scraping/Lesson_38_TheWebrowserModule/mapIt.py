# Import relevant modules
import webbrowser, sys, pyperclip

# Create a List Variable
sys.argv # ['mapIt.py', '870', 'Valencia', 'St.']

# Check if command line arguments were passed
if len(sys.argv) > 1:
    # ['mapIt.py', '870', 'Valencia', 'St.'] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])          # Join the Arguments into a Single String variable called address
else:
    address = pyperclip.paste() # If additional string arguments were not passed, then utilize the Clipboard value

# Utilize webbrowser.open() to Navigate to Google Maps and pass the address variable (https://www.google.com/maps/)place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)
