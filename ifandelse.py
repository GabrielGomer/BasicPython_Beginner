people = 50
drone = 40
plane = 64
# Determining whether Boolean Expression is True or False
if drone > people:
    print("We should take the drone.")
elif drone < people:
    print("We should not take the drones.")
else:
    print("We can't decide.")
if plane > drone:
    print("That's too many planes.")
elif plane < drone:
    print("Maybe we could take the plane.")
else:
    print("We still can't decide")
if people > plane:
    print("Alright, let's just take the plane.")
else:
    print("Fine, let's stay home then.")