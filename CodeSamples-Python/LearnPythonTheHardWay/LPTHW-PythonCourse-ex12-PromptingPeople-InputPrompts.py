# prompt on-screen a question and save the value
age = input("How old are you? ")

# prompt on-screen a question and save the value
height = input(f"You're {age}? Nice. How tall are you? ")

# prompt on-screen a question and save the value
weight = input("How much do you weight? ")

# print to screen the results from the questions
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# print to screen indication we're going to try something new
print("\nWe're going to try something a little more fun now!")

# print to screen a question: What Class does the user like to play in Diablo 3?
d3Class = input("\nThe new Diablo 3 Season starts today! Which Class are you going to choose?! ")

# print to screen a question: What role does the user like to execute in group content
d3Style = input(f"\nSo you like {d3Class}, cool. In group content, what role do you like to play? ")

# print to screen a question: What is their favorite Item
d3Item = input(f"\nDo you have a favorite Item for your {d3Class} when you play {d3Style}? ")

#print to screen their responses
print(f"\nSo you like to use your {d3Item} to {d3Style} with your {d3Class}?! Thats cool! ")