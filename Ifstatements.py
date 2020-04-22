people = 20
bikes = 30
skateboard = 15

if people < bikes:
    print("There are enough bikes for everyone.")
if people > bikes:
    print("The remaining will walk.")
if people < skateboard:
    print('Make sure to wear your safety gear')
if people > skateboard:
    print("Take turns skating")
"""
+= or -=
+= ? the code x = x +1 
x +=1 involves less typing 
"""
skateboard +=5
if people >= skateboard:
    print("People are greater than or equal to skateboards")
if people <= skateboard:
    print("People are less than or equal to skateboards")
if people == skateboard:
    print("People are skateboards.")