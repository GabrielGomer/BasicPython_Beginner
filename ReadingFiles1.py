# Reading Files
# You know how to get input from a user with input() or argv
# What can you do to get filename information (file path)>
# The solution is to use argv or input() to ask the user what file to read or write from
# to open instead of hard coding the file's name
from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}: ")
print(txt.read())

print("Type the filename again: ")
file_again = input("> ")
txt_again = open(file_again)

print(txt_again.read())