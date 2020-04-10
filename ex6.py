# variable assignment
types_of_people = 10

# string with variable assign
x = f"There are {types_of_people} types of people." # <-- drill2 (1 out 4)

# String assigned to variable
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}" # <-- drill2 (2 out 4)

# Print variables x and y
print(x)
print(y)

# print formated strings
print(f"I said: {x}")  # <-- drill2 (3 out 4)
print(f"I also said: '{y}'")  # <-- drill2 (4 out 4)

# Boolean variable assignment
hilarious = True
joke_evaluation = "Isn't that joke so funny?! {}" # <-- drill2 (5 out 4), yes you are lying :)

# print formated String
print(joke_evaluation.format(hilarious)) # <-- drill2 (6 out 4), yes you are lying :)  

# print changing format() to see the result
print(joke_evaluation.format("I'm from format()"))

w = "This is the left side of..."
e = "a string with right side."

# drill 4: Concatenating 2 strings.
print(w + e)