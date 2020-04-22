"""
When to use Lists
1) If you need to maintain order.
This is a listed order, not a sorted order.
Lists do not sort for you.
2) If you need to access the contents randomly by a number.
Remember, this is using cardinal numbers starting at 0.
3) If you need to go through the contents linearly (first to last).
Remember that's what for-loops are for.
"""
ten_things = "Apples Oranges Bird Iphone Coffee Sugar"
# " Apples"," Oranges", Bird Iphone Coffee Sugar Tennis Girl Orange Pizza
print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Football",
              "Pizza", "Orange", "Girl", "Tennis"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))











