# A screenshot is an image of the screen's content.
# The pyautogui.screenshot() will return an Image object of the screen, or you can pass it a filename to save it to a file
# locateOnScreen() is passed a sample image file, and returns the coordinates of where it is on the screen.
# locateCenterOnScreen() will return an (x, y) tuple of where the image is on the screen.
# Combining the keyboard/mouse/screenshot functions lets you make awesome stuff!

# Import relevant modules
import pyautogui, os, subprocess

# Update Working Directory to Local Lesson Folder where the example.xlsx file resides
os.chdir('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_16_GUIAutomation\\Lesson_50_ScreenshotsImageRecognition')

# Verify the Current Working Directory
filePath = os.getcwd()

# DEBUG Print the Current Working Directories File Path
print(filePath)

# Take a Screenshot and save it locally in the Current Working Directory
pyautogui.screenshot('screenshot_example.png')

# Utilize Subprocess.Popen() to launch the Windows default Calc.exe
try:
    subprocess.Popen("calc.exe")
except FileNotFoundError:
    print("Error: calc.exe not found. Ensure it's in your system's PATH.")
except Exception as e:
    print(f"An error occurred: {e}")

# Locate a UI Element presently displayed onscreen based upon a Pixel accurate source PNG Image utilizing pyautogui.locateOnScreen()
imgCordOnScreen1 = pyautogui.locateOnScreen('calc8key.png', minSearchTime=2, confidence=.8)               # Utilize IF target image == Current Working Directory where the Py Script is being executed
imgCordOnScreen2 = pyautogui.locateOnScreen('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_16_GUIAutomation\\Lesson_50_ScreenshotsImageRecognition\\calc8key.png', minSearchTime=2, confidence=.8)                                                                     # Utilize IF target image == Current Working Directory != where the Py Script is being executed

# DEBUG Print
print(imgCordOnScreen1)
print(imgCordOnScreen2)

# Locate the Center Cords of a UI Element presently displayed onscreen based upon a Pixel accurate source PNG Image utilizing pyautogui.locateCenterOnScreen()
imgCenterCordOnScreen1 = pyautogui.locateCenterOnScreen('calc8key.png', minSearchTime=2, confidence=.8)               # Utilize IF target image == Current Working Directory where the Py Script is being executed
imgCenterCordOnScreen2 = pyautogui.locateCenterOnScreen('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_16_GUIAutomation\\Lesson_50_ScreenshotsImageRecognition\\calc8key.png', minSearchTime=2, confidence=.8)                                                  # Utilize IF target image == Current Working Directory != where the Py Script is being executed

# DEBUG Print
print(imgCenterCordOnScreen1)
print(imgCenterCordOnScreen2)

# moveTo() and Click()
pyautogui.moveTo(imgCordOnScreen1, duration=1)
pyautogui.moveTo(imgCordOnScreen2, duration=1)
pyautogui.moveTo(imgCenterCordOnScreen1, duration=1)
pyautogui.moveTo(imgCenterCordOnScreen2, duration=1)
pyautogui.click((imgCordOnScreen1), duration=1)
pyautogui.click((imgCordOnScreen2), duration=1)
pyautogui.click((imgCenterCordOnScreen1), duration=1)
pyautogui.click((imgCenterCordOnScreen2), duration=1)