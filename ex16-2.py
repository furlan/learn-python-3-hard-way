from sys import argv

script, filename = argv

file = open(filename)

print(f"Here is the file {filename}: ")
print(file.read())
file.close()