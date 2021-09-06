def add(a, b):
  print(f"ADDING {a} + {b}")
  return a + b

def subtract(a, b):
  print(f"SUBTRACTING {a} - {b}")
  return a - b

def multiply(a, b):
  print(f"MULTIPLYING {a} * {b}")
  return a * b

def divide(a, b):
  print(f"DIVIDING {a} / {b}")
  return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzze for extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That become: ", what, "Can you do it by hand?")

puzzle = age + (height - (weight * (iq / 2)))
print(f"Puzze by hand: {puzzle}")

puzzle2 = 30 + 5 + ((78 - 4) - ((90 * 2) * ((100 / 2) / 2)))
print(f"Another way: {puzzle2}")

inverse = 40 + 2 - 89 * 40 / 2
print(f"Inverse formula by hand: {inverse}")

inverse2 = add(40, subtract(2, multiply(89, divide(40, 2))))
print(f"Inverse with functions: {inverse2}")