# PyAutoGUI's virtual key presses will go the window the currently has focus.
# typewrite() can be passed a string of characters to type. It also has an "interval" keyword argument.
# Passing a list of strings to typewrite() lets you use hard-to-type keyboard keys, like ‘shift' or ‘f1'.
# These keyboard key strings are in the pyautogui.KEYBOARD_KEYS list.
# pyautogui.press() will press a single key.
# pyautogui.hotkey() can be used for keyboard shortcuts, like Ctrl-O.

# Import relevant modules
import pyautogui, os

# Update Working Directory to Local Lesson Folder where the example.xlsx file resides
os.chdir('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_16_GUIAutomation\\Lesson_49_ControllingTheKeyboardFromPython')

# Verify the Current Working Directory
filePath = os.getcwd()

# DEBUG Print the Current Working Directories File Path
print(filePath)

# Click to pass Focus to a viable GUI, then utilizing pyautogui.typewrite() to send Keystrokes
pyautogui.click(100,100); pyautogui.typewrite('Hello world!')

# Click to pass Focus to a viable GUI, then utilizing pyautogui.typewrite() to send Keystrokes with an interval
pyautogui.click(100,100); pyautogui.typewrite('Hello world!', interval=.2)

# Click to pass Focus to a viable GUI, then utilizing pyautogui.typewrite() to send a series of Keystrokes and Keyboard actions
pyautogui.click(100,100); pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval=1)

# Identify the Screen Resolution Size
keyboardKeys = pyautogui.KEYBOARD_KEYS

# Print Debug Variable Data
print(keyboardKeys)

# Send a distinct Keyboard input with pyautogui.press()
pyautogui.press('f1')

# Send a distinct Hotkey combination with pyautogui.hotkey()
pyautogui.hotkey('ctrl', 'o')