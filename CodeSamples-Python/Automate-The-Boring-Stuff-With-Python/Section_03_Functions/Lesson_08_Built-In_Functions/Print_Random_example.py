# Import a single module
# import random

# Import multiple modules at once 
import random, sys, os, math        # Function calls from modules imported this way need to be prefaced by the module name

# Import all the Functions associated with a given module
from random import *                # Function calls from modules imported this way do NOT need to be prefaced by the module

# Create a for loop to print random #'s
for i in range(5):
    print(random.randint(1, 10))
