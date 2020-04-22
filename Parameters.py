# Let's pass variables into a script
from sys import argv

script, first, second, third = argv

# This process is called unpacking and then it packs/set the variables
print("The script is called: ", script)
print("Your first variable is:", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)
