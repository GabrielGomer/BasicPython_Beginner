# What's a Data Structure
# iF you think about it, a data structure is just a formal way to
# structure(organize) some data.
# A way to store facts inside a program so you can access them
# in different ways,
# They structure data.

# A dictionary (dicts) is a way to store data just like a list,
# but instead of using only numbers to get the data
# you can almost anything.
# Lets you treat a dict like it's a database for
# storing and organizing data.

# create a mapping of state to abbreviation
states = {
    'New Mexico': 'NM',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
# create a basic set of states and some cities in them
cities = {
    'CA':  'San Francisco',
    'MI': "Detroit",
    'FL': "Jacksonville"
}
# add some more cities
cities['NY'] = 'New York'
cities['NM'] = 'Santa Fe'

# print out some cities
print('-'*10)
print("NY State has: ", cities['NY'])
print("NM State has: ", cities['NM'])

# print some states
print('-'*10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-'*10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print ever state abbreviation
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-'*10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

# get a abbreviation by state that might not be there
print('-'*10)
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# Get a city with a default value.
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")




























