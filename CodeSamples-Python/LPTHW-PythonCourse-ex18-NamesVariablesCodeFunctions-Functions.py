# this one is like your scripts with argv
# define the function print_two
def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
# define the function print_two_again
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
# define the function print_one
def print_one(arg1):
	print(f"arg1: {arg1}")

# this one takes no arguments
# define the function print_none
def print_none():
	print("I got nothin'.")

# execute each of the newly created functions by passing in the correct # of arguments
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()