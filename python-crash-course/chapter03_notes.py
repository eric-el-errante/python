# Lists are collections of items in particular order. Since lists are usually
# more than one item, the name of a list tends to be plural.
# Square brackets indicate a list, and elements are separated by commas.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# To access a particular element, you use the index of the item.
print(bicycles[0])  # Note the first element in a list has an index of 0, not 1
print(bicycles[2])
print(bicycles[1].title())

print(bicycles[-1]) # Index of -1 will return the LAST element in a last always
print(bicycles[-2]) # This returns the 2nd to LAST element in a list, etc

# Each individual value in a list can be use like any other variable.
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

# change the value of an item in a list 
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'   # This changes the first item
print(motorcycles)

# adding elements to a list using appends adds to the end of list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

# you can use an empty list and then add elements to it
motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# add to a specific position using .insert(#, value)
# note, this will insert the value to the specified position and move all
# other values one position to the "right"
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.insert(0,'ducati')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.insert(2,'ducati')
print(motorcycles)

# removing items from a list knowing it's position
# once something is deleted, it is gone forever
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]  # del list[#] will delete an item from specified position
print(motorcycles)

# the pop method allows you told hold on to the information after it is
# popped
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop() # the last item in the list is popped
# and assigned to a new variable
print(motorcycles)
print(popped_motorcycles)

# you can also pop off any element in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
first_owned = motorcycles.pop(1)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# you can also remove an item by its VALUE, not is POSITION
# this only removes ONE INSTANCE of the value, not all
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# The sort() method makes it easy to sort a list. It will alphabetically sort
# a list PERMANENTLY

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True) # This will permanently sort the list in reverse order
print(cars)

# The sorted() function does NOT permanently alter a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:", cars)
print("Here is the list using sorted():", sorted(cars))
print("Here is the original list:", cars)

# the reverse() function will put a list in reverse order, not alphabetical
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("This is the original list:", cars)
cars.reverse()
print("This is the list using reverse():", cars)
cars.reverse()
print("This is the list again using the reverse():", cars)

# use len() to find the length of a list, that is, the number of elements
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

