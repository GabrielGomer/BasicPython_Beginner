formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", 'two', 'three', 'four', 'five'))
print(formatter.format(True, False, False, True)) # These values are called boolean values: True or False
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Have yourself",
    "a merry little christmas",
    "santa claus is coming to town",
    'ok'
))

# Print out days and months
days = "Mon Tue Wed Thur Fri Sat Sun"
# \n
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
    Todo List:
        * Brush Teeth
        * Stretch arms and legs
        *Go to School
        *Do Homework
        * Play with Friends
        *Hug Mom
        *Sleep
""")
