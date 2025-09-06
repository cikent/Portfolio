# Controlling the mouse and keyboard is called GUI automation.
# The PyAutoGUI third-party module has many functions to control the mouse and keyboard.
# pyautogui.size() returns the screen resolution, pyautogui.position() returns the mouse position. These are returned as tuples of two integers.
# pyautogui.moveTo(x, y) moves the mouse to an x, y coordinate on the screen.
# The mouse move is instantaneous, unless you pass an int for the "duration" keyword argument.
# pyautogui.moveRel() moves the mouse relative to its current position.
# PyAutoGUI's click(), doubleClick(), rightClick(), and middleClick() click the mouse buttons.
# dragTo() and dragRel() will move the mouse while holding down a mouse button.
# If your program gets out of control, quickly move the mouse cursor to the top-left corner to stop it.
# There's more documentation at pyautogui.readthedocs.org.

# Import relevant modules
import pyautogui, os

# Update Working Directory to Local Lesson Folder where the example.xlsx file resides
os.chdir('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_16_GUIAutomation\\Lesson_48_ControllingTheMouseFromPython')

# Verify the Current Working Directory
filePath = os.getcwd()

# DEBUG Print the Current Working Directories File Path
print(filePath)

# Identify the Screen Resolution Size
screenResolution = pyautogui.size()

# Print Debug Variable Data
print(screenResolution)

# Utilize Multiassignment to cast the Screen Resolution to distinct values
width, height = pyautogui.size()

# Print Debug Variable Data
print(str(width) + ' x ' + str(height))

# Identify current Mouse Cursor Position
mousePosition = pyautogui.position()

# Print Debug Variable Data
print(mousePosition)

# Move the Mouse Coursor to a given XY Coordinate location; 1st Argument = X Coordinate, 2nd Argument = Y Coordinate
pyautogui.moveTo(250, 250)

# Move the Mouse Coursor to a given XY Coordinate location; 1st Argument = X Coordinate, 2nd Argument = Y Coordinate, 3rd Argument = Duration
pyautogui.moveTo(10, 10, duration=1.5)

# Move the Mouse Coursor Relative to its Current Onscreen location; 1st Argument = X Coordinate Offset, 2nd Argument = Y Coordinate Offset
pyautogui.moveRel(50, 50)

# Move the Mouse Coursor Relative to its Current Onscreen location; 1st Argument = X Coordinate Offset, 2nd Argument = Y Coordinate Offset, 3rd Argument = Duration
pyautogui.moveRel(500, 500, duration=2)

# Move the Mouse Coursor Relative to its Current Onscreen location; 1st Argument = X Coordinate Offset, 2nd Argument = Y Coordinate Offset, 3rd Argument = Duration
pyautogui.moveRel(0, -100, duration=1)

# Move the Mouse Coursor to a given XY Coordinate location; 1st Argument = X Coordinate, 2nd Argument = Y Coordinate, 3rd Argument = Duration
pyautogui.click(116, 300, duration=1.5)

# Via Terminal | PowerShell, utilize the pyautogui.displayMousePosition() function to dynamically and continously display the Cursor's current X & Y position
# pyautogui.displayMousePosition()
