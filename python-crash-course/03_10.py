# Every Function: Think of something you could store in a list. For example,
# you could make a list of mountains, rivers, countries, cities, languages,
# or anything else you'd like. Write a program that creates a list containing
# these items and then uses each function introduced in this chapter at least
# once.

parks = ['arches', 'canyonlands', 'capitol reef', 'bryce canyon', 'zion']
print("This is a list of National Parks, in no particular order:", parks)
print("This is the third National Park in the list:", parks[2])

parks.append('great basin')
print("This is the new list, with appended value:", parks)

parks.insert(2,'rocky mountains')
print("This is the new list with an inserted value:", parks)

del parks[1]
print("This is the new list with one value deleted:", parks)

popped_park = parks.pop(2)
print("This is the new list with an item popped:", parks)

parks.remove('zion')
print("This is the new list with an exact value removed:", parks)

parks.sort()
print("Sorted in alphabetical order:", parks)
parks.sort(reverse=True)
print("Sorted in reverse alphabetical order:", parks)

parks = ['arches', 'canyonlands', 'capitol reef', 'bryce canyon', 'zion']
print("This is the list using temporary sort:", sorted(parks))
print("Original list:", parks)
parks.reverse()
print("List in reverse order:", parks)
print("Number of values in the list:",len(parks))