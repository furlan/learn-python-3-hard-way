from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}...")
out_file = open(to_file, 'w').write(open(from_file).read())

print("Alright, all done!")
out_file.close()