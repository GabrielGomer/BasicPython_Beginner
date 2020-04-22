# Copying Files
# Goal is to copy contents/txt from the from_file -> to_file
# We will use argv to get both files from user instead hard coding
# This will make the code more reusable
# Since python doesnt have a copy function we will be programming it ourselves
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")
in_file = open(from_file)
indata = in_file.read()
# The len() function gets the length of the string that you pass to it then returns
# that as a number. play with it
print(f"The input file is { len(indata) } bytes long")
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN or ENTER to continue, CTRL-C to abort")
input()
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done copying.")
out_file.close()
in_file.close()
