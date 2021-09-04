# import argv module with alias name foo and bound locally (to the local namespace)   
# more practice to understand modules: fibo.py
from sys import argv as foo

# load each variable with the arguments passed
script, filename = foo

# open the file and return a stream to txt variable
txt = open(filename)

# show message with file name.
print(f"Here's your file {filename}: ")
# show the file content.
print (txt.read())
txt.close()

# request an input for a new file name.
print("Type the filename again:")
file_again = input("> ")

# open the new file and return a stream to txt_again variable
txt_again = open(file_again)

# show the new file content.
print(txt_again.read()) 
txt_again.close()
