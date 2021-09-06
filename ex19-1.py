# Define a function to print text about the amount of cheese and amount of boxes of crackers.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print(f"You have {cheese_count} cheeses!")
  print(f"You have {boxes_of_crackers} boxes of crackers!")
  print("Man that's enough for a party!")
  # Last statement of the function
  print("Get a blanket.\n")

print("We can just give the function numbers directly:")
# execute function passing 2 literals intergers.
cheese_and_crackers(20, 30)

print("OR can just give the function numbers directly:")
# create two variables
amount_of_cheese = 10
amount_of_crackers = 50

# execute the function using the variables created.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
# execute the function using the result of the 2 expressions as input.
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
# execute the function using the result of the 2 expressions using literals and variables.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)