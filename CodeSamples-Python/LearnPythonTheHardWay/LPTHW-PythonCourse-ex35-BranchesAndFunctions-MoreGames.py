# import the Module exit from the Sys Library
from sys import exit

# def the function gold room
def gold_room():
	# print to screen a question
	print("This room is full of gold. How much do you take?")

	# store the User's input to the question
	choice = input("> ")
	# evaluate the User's input and perform conditional actions based upon their response
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print("Nice, you're not greedy, you win!")
		exit(0)
	else:
		dead("You greedy bastard!")

# def the function bear_room
def bear_room():
	# print to screen a series of prompts followed by a question
	print("There is a bear here.")
	print("The bear has a bunch of honey.")
	print("The fat bear is in front of another door.")
	print("How are you going to move the bear?")
	# store intial state of whether or not the Bear has moved from the default position
	bear_moved = False

	# cause this logic to continually execute while the Bear_room function / method is being run
	while True:
		# store the User's input to the question
		choice = input("> ")

		# evaluate the User's input and perform conditional actions based upon their response
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print("The bear has moved from the door.")
			print("You can go through it now.")
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			dead("I got no idea what that means.")

# def the function cthulhu_room
def cthulhu_room():
	# print to screen a series of prompts followed by a question
	print("Here you see the great evil Cthulhu.")
	print("He, it, whatever stares as you and you go insane.")
	print("Do you flee for your life or eat your head?")

	# store the User's input to the question
	choice = input("> ")

	# evaluate the User's input and perform conditional actions based upon their response
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

# def the function dead
def dead(why):
	print(why, "Good job!")
	exit(0)

# def the function start
def start():
	# print to screen a series of prompts
	print("You are in a dark room.")
	print("There is a door to your right and left.")
	print("Which one do you take?")

	# store the User's input to the question
	choice = input("> ")

	# evaluate the User's input and perform conditional actions based upon their response
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")

# execute the method / function 'Start' to being the game
start()