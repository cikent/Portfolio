'''
The wonderful world of Pokemon
'''

# create a list with the Pokemon the player currently owns
player_owned_pokemon = []
rival_owned_pokemon = []

# debug print
# print(player_owned_pokemon)

# Function for the Pokemon Intro
def pokemon_intro():
	print("\nWelcome to the world of Pokemon!")
	print("Today you get to pick your first Pokemon.")
	print("Your choices are: Charmander, Bulbasaur and Squirtle.")

# Function for choosing a 1st pokemon
def player_choose_pokemon():
	print("Which would you like to choose? Please type their name.")
	pokemon_choice = input("> ")

	if pokemon_choice == "Charmander":
		print(f"Awesome, you've chosen the Fire Pokemon {pokemon_choice}!")
		player_owned_pokemon.append(pokemon_choice)
		return player_owned_pokemon
	elif pokemon_choice == "Bulbasaur":
		print(f"Awesome, you've chosen the Grass Pokemon {pokemon_choice}!")
		player_owned_pokemon.append(pokemon_choice)
		return player_owned_pokemon	
	elif pokemon_choice == "Squirtle":
		print(f"Awesome, you've chosen the Water Pokemon {pokemon_choice}!")
		player_owned_pokemon.append(pokemon_choice)
		return player_owned_pokemon
	else:
		print("Please choose one of the options available: Charmander, Bulbasaur or Squirtle.")
		player_choose_pokemon()

# Function for the Rival's pokemon to be picked based upon the Player's initial choice
def rival_choose_pokemon(player_owned_pokemon):
	print("\nYour Rival get's to choose their Pokemon now.")
	print("Your Rival walks up to the table and selects a Pokemon.")
	print("Your Rival says: \"This one is mine and its stronger, I know it!\"")

	if player_owned_pokemon == "Charmander":
		rival_owned_pokemon.append("Squirtle")
		return rival_owned_pokemon
	elif player_owned_pokemon == "Bulbasaur":
		rival_owned_pokemon.append("Charmander")
		return rival_owned_pokemon	
	else:
		rival_owned_pokemon.append("Bulbasaur")
		return rival_owned_pokemon

# Function to prompt the player with their 1st choice after having picked a pokemon
def player_action_prompt():
	print("\nNow that you have your 1st Pokemon, what do you want to do next!?")
	print("Option 1: Battle your Rival?!")
	print("Option 2: Explore Town for more items?")
	print("Option 3: Venture into the Wild and find more Pokemon!")

# Function to assess what the players Choice is to the Question
def player_action():
	print("\nPlease choose either Option 1, 2 or 3!")
	player_1st_choice = input("> ")

	if player_1st_choice == "1":
		print("Time to pick a fight!")
		# challenge_rival()
	elif player_1st_choice == "2":
		print("Time to look for hidden goodies!")
		# explore_town()
	elif player_1st_choice == "3":
		print("Time to fill that Pokedex!")
		# search_for_pokemon()
	else:
		print("That isn't an option. Try again.")
		player_action_prompt()
		player_action()
'''
def challenge_rival():
	# print("Hey! So you think your Pokemon is strong? Prove it!")

def explore_town():

def search_for_pokemon():
'''

# run intro
pokemon_intro()

# Ask the player to choose their first pokemon
player_choose_pokemon()

# debug print
# print("Player owned Pokemon is: ", player_owned_pokemon[0])

# Now the Rival Chooses their Pokemon
rival_choose_pokemon(player_owned_pokemon[0])

# debug print
# print("Rival owned Pokemon is: ", rival_owned_pokemon[0])

# Ask the player what their first Action will be now that they have a Pokemon
player_action_prompt()

# execute the players Action
player_action()