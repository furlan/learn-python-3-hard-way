import math

name = 'Flavio Furlan'
age = 41 # ok, boomer
height = 180 # centimeters
weight = 190 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.")
print(f"He's {height} centimeters tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this lins it tricky, tro to get it exacly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}")

# convert to inches
height_in = round(height / 2.53)

print(f"He's height in inches is {height_in}")

# convert to kg
weight_kg = round(weight / 2.205)
print(f"He's weight in kg is {weight_kg}")
