i = 0
numbers = []
limit_txt = input("Enter the limit > ")
limit = int(limit_txt)

def main(numbers, i, limit):
  if i < limit:
    append_number(i)
    i += 1
    return main(numbers, i, limit)

def append_number(num):
  numbers.append(num)

main(numbers, i, limit)

print("The numbers: ")

for num in numbers:
  print(num)