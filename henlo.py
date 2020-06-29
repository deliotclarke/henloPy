from numpy import array

msg = "Henlo Snakes!"
print(msg)

# playing in cars with pythons
cars = ['El Camino', 'El Camino', 'El Camino']

# simple printing loop
for x in cars:
    print(x)

# add an item to a list
cars.append('Bob Marley')

# the ol loop and print
for x in cars:
    print(x)

# storing a value at an index in list
y = cars[3]

#  you guessed it
print(y)

# printing the length of a list
print(len(cars))

# copy the contents of the list
cars2 = cars.copy()

# clear contents of a list
cars.clear()

# is it real?
print("cars length: ", len(cars))
print("cars 2 length: ", len(cars2))

# count() stores the instances of a value in your list
print("El Camino Count: ", cars2.count("El Camino"))

# a dictionary!!
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1967
}

# print it
print(thisdict)

# print just the value of a key in the dictionary
print(thisdict["model"])

# changing the value of a key in said dictionary
thisdict["year"] = 1965

# sometimes you've got to print to check
print(thisdict)

# looping a dictionary's keys
for x in thisdict:
    print(x)

# looping a dictionary's values
for x in thisdict:
    print(thisdict[x])

# looping both, but with a conditional to only pring if the key is "model"
for x, y in thisdict.items():
    if x is "model":
        print(x, y)

cost = [4, 8, 12, 16, 20, 100, 120, 60, 13]

# not possible with lists - going to import array from numpy to try again
# divided_cost = cost/2

# print(divided_cost)

# works! super interesting
cost2 = array([4, 8, 12, 16, 20, 100, 120, 60, 13])

divided_cost2 = cost2/2

print(divided_cost2)
