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

