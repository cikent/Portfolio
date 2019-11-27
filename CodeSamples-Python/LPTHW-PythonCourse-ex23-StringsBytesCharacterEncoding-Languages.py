# import system module
import sys
# unpack argv into various parameters
script, input_encoding, error = sys.argv

# define the function main
def main(language_file, encoding, errors): # has 3 parameters
	print(">>>> main", repr(language_file), encoding, errors)
	line = language_file.readline()

	if line:
		print(">> there's a line", repr(line))
		print_line(line, encoding, errors)
		print(">> calling main again")
		return main(language_file, encoding, errors)
	print("<<<< exit main")

# define the function print_line
def print_line(line, encoding, errors):
	next_lang = line.strip()
	raw_bytes = next_lang.encode(encoding, errors=errors)
	cooked_string = raw_bytes.decode(encoding, errors=errors)

	print(raw_bytes, "<===>", cooked_string)

# open the specified file and store it in a file object
languages = open("languages.txt", encoding="utf-8")

# execute main using the necessary parameters
main(languages, input_encoding, error)