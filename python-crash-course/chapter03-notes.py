# Lists use brackets and are in a particular order
cars = ['toyota', 'nissan', 'jeep', 'honda', 'ford', 'chevrolet']
print(cars)

# this pulls out elements 0 and 4 from the list
print(cars[0])
print(cars[4])
print(cars[3].title())

# using list[-1] will always display the last element in a list
# -2 would do second to last, -3 third to last
print(cars[-1])

# pulling individual values and using f-strings
message = f'My first car was a {cars[1].title()}.'
print(message)

# modifying elements in a list
print('the cars list is: ', cars)
print('cars[2] =', cars[2])
cars[2] = 'mercedes'
print("after cars[2] = 'mercedes', then list cars is...", cars)

# adding elements in a list
cars.append('porsche')
print("After cars.append('porsche'), 'porsche' is added to the end of the list:", cars)

motorcycles = []                # creates an empty list
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# you can insert elements to a particular spot in a list
# this will insert it at the designated index, and move all elements after it
# to the right one spot
motorcycles.insert(1, 'ducati')
print(motorcycles)

# removing items, if you know the index number
del motorcycles[1]
print(motorcycles)

# you can 'pop' off any value in a list
# that will remove it from the list, but still keep it to be used later
print(motorcycles)
popped_motorcycle = motorcycles.pop(1)          # specify which index number you want gone
print(motorcycles)
print(popped_motorcycle)

# removing by value rather than index ***** THIS ONLY REMOVES THE FIRST VALUE, NOT SUBSEQUENT ONES *****
cars = ['toyota', 'nissan', 'jeep', 'honda', 'ford', 'chevrolet']
print(cars)
cars.remove('jeep')
print(cars)

# organizing a list SORT METHOD WILL PERMANENTLY MODIFY A LIST

print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)                 # passing this argument will put the list in reverse order
print(cars)

# sort function will not permanently change a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('original list: ', cars)
print('sorted list: ', sorted(cars))
print('original list: ', cars)

# reverse method reverses the order of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# length of a list len(list)
print(len(cars))