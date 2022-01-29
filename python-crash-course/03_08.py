# Seeing the world: Think of at least five places in the world you'd like to
# visit.

# Store the locations in a list. Make sure it is not in alphabetical order.
places = ['utah','new zealand','big bend national park', 'dakotas', 'idaho']

# Print you list in its orignal order. Don't worry about printing the list
# neatly, just print it as a raw Python list.
print(places)

# Use sorted() to print your list in alphabetical order without modifying the
# actual list
print(sorted(places))

# Show that your list is still in its original order by printing it.
print(places)

# Use sorted() to print your list in reverse alphabetical order without changing
# the order of the original list
print(sorted(places,reverse=True))

# Show that your list is still in its original order by print it.
print(places)

# Use reverse() to change the order of your list. Print the list to show
# that it's order has changed
places.reverse()
print(places)

# Use the reverse() to change the order of your list again. Print the list to
# show it is back to its original order
places.reverse()
print(places)

# use the sort() function to change your list so it's stored in alphabetical
# order. print the list to show that its order has been changed
places.sort()
print(places)

# use sort() to change your list so it's stored in reverse alphabetical order
# print the list to show the order has been changed
places.sort(reverse=True)
print(places)