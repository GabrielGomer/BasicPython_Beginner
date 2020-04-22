# Asking Questions

# We put end=' ' at the end of each print line.
# This tells print to not end the line with a newline character and go to the next line

print("How old are you?", end=' ')
age = int(input())
print("What sports do you play?", end=' ')
sports = input()
print("What is your most favorite drink or food?", end=' ')
favorite_food = input()

name = input("What is your name? ")
work = input("What do you want to do in the future? ")
animal = input("What is your most favorite animal? ")
print(f"Hi my name is {name}. I work as a {work} and live with my three {animal}.")
