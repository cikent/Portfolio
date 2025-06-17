# prompting the user with the initial description of the Scripts behavior
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

# declaring a String multi-line variable
poem = """
\tThe lovely world
with logic so firmly planted 
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation.
\n\t\twhere there is none.
"""

# print to screen the variable poem contains in 2 other strings
print("----------------")
print(poem)
print("----------------")
 

# delclare the Integer variable five
five = 10 - 2 + 3 - 6
print(f"This should be {five}")

# define the function secret_formula
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars /100
	# return Jelly Beans, Jars and Crates
	return jelly_beans, jars, crates

# declare the variable Start Point
start_point = 10000
beans, jars, crates = secret_formula(start_point)

# example of creating a Format String using the Function
# remember that this is another way to format a string.
print("With a starting point of: {}".format(start_point))
# example of creating a Format String using the Print Function with a format argument on the String inputted.
# it's jus like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# divide the Start Point variable by 10
start_point = start_point / 10

# example of Format String with two previous examples combined
print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a lis to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))