i = 0
numbers = []

limit_txt = input("Limit > ")
limit = int(limit_txt)
step_txt = input("Steps > ")
step = int(step_txt)

def main(numbers, i, step, limit):
  if i < limit:
    append_number(i)
    i += step
    return main(numbers, i, step, limit)

def append_number(num):
  numbers.append(num)

main(numbers, i, step, limit)

print("The numbers: ")

for num in numbers:
  print(num)