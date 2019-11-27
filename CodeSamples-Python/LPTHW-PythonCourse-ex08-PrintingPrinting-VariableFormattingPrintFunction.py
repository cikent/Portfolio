# declare a String w/ 4 Format Command brackets inside
formatter = "{} {} {} {}"

# print formatter to screen with new Integers
print(formatter.format(1, 2, 3, 4))
# print formatter to screen with new Strings
print(formatter.format("one", "two", "three", "four"))
# print formatter to screen with new Boolean values
print(formatter.format(True, False, False, True))
# print formatter to screen using itself as the 4 argument's
print(formatter.format(formatter, formatter, formatter, formatter))

# print formatter to screen with new Strings, broken onto new lines
print(formatter.format(
	"I love you beyond", 
	"What words can express",
	"Actions can show",
	"Or time will tell",
))