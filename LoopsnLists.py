the_count = [1, 2, 3, 4, 5]
fruits = ['berry', 'oranges', 'pears', 'kiwi']
lang = ['spanish', 'english', 'mandarin', 100]

for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

    # also we can go through mixed lists too

for i in lang:
    print(f"I can speak {i}.")
# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that list understand
    elements.append(i)

# 2D two dimensional list
two_dimensional = [[1, 2, 3], [4, 5, 6]]
