# Create functions for ADD, SUBTRACT, Multiply, division
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b


def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b


def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions. ")
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2) # 50
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
# A puzzle for the extra credit, Type it
print("Here is a puzzle")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand?")
# divide(50, 2) = 25
# multiply(180, 25) = 4500
# subtract(74, 4500) = 74-4500=-4426
#add(35, -4426)=-4391