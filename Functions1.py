# Functions
# Have finite number of steps
# Have a return statements
# Has only one task to complete


def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


# this justs takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")


def print_none():
    print("I got nothin.")


print_two("Red", "Robin")
print_two_again("Red", "Cabin")
print("Red")
print_none()


