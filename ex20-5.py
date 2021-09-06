# import argv from sys module and bound locally
from sys import argv

# read the script input arguments
script, input_file = argv

# define a function to print the all lines of a text file passed in the parameter.
def print_all(f):
  print(f.read())

# define a function to set the file cursor in the first line.
def rewind(f):
  f.seek(0)

# define a function to print the content of actual cursor line.
def print_a_line(line_count, f):
  print(line_count, f.readline(), end="")

# open the file passes in the scripts arguments
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 0

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)