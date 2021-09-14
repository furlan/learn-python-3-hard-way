numbers = []
limit_txt = input("Enter the limit > ")
limit = int(limit_txt)

for i in range(0, limit):
  numbers.append(i)

print("The numbers: ")

for num in numbers:
  print(num)