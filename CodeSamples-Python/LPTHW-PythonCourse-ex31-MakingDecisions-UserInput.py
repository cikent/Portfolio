# Print to screen information about spawn location
print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

# store User's input for door
door = input("> ")

# determine if User input is 1 or not; if 1, execute Code block below
if door == "1":
	print("There's a giant bear here eating a cheese cake.")
	print("What do you do?")
	print("1. Take the cake.")
	print("2. Scream at the bear.")

	# store User's input for bear
	bear = input("> ")

	# If-Statement based upon bear's value
	if bear == "1":
		print("The bear eats your face off. Good job!")
	elif bear == "2":
		print("The bear eats your face off. Good job!")
	else:
		print(f"Well, doing {bear} is probably better.")
		print("Bear runs away.")

# determine if User input is 2 or not; if 2, execute Code block below
elif door == "2":
	print("You stare into the endless abyss at Cthulhu's retina.")
	print("1. Blueberries.")
	print("2. Yellow jacket clothespins.")
	print("3. Understanding revolvers yelling melodies.")

	# store User's input for insanity
	insanity = input("> ")

	# If-Statement based upon insanity's value
	if insanity == "1" or insanity == "2":
		print("Your body survives powered by a mind of jello.")
		print("Good job!")
	else:
		print("The insanity rots your eyes into a pool of muck.")
		print("Good job!")

# Execute if Door User input is anything != to 1 OR 2
else:
	print("You stumble around and fall on a knife and die. Good job!")