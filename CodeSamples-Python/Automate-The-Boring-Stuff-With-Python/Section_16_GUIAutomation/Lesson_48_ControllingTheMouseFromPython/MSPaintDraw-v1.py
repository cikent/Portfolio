# Import relevant modules
import pyautogui

# TODO Ensure MS Paint is Launched

# Initiate the Drawing Animation
pyautogui.click()                   # Click to ensure drawing program has focus on MS Paint

# Define an initial Distance
distance = 200

# Create a While Loop to draw the shape
while distance > 0:
    print(distance, 0)
    pyautogui.dragRel(distance, 0, duration=0.1)        # Move cursor to the right
    distance = distance - 25
    print(0, distance)
    pyautogui.dragRel(0, distance, duration=0.1)        # Move cursor to the down
    print(-distance, 0)
    pyautogui.dragRel(-distance, 0, duration=0.1)        # Move cursor to the left
    distance = distance - 25
    print(0, -distance)
    pyautogui.dragRel(0, -distance, duration=0.1)        # Move cursor to the up
