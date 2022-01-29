# Slices: Using one of the programs you wrote in this chapter, add several lines
# to the end of the program that do the following:

animals = ['dog', 'cat', 'horse','coyote', 'bear', 'mountain lion']
for animal in animals:
    print(f"Would a {animal} make a good pet?")
print("All these animals have four legs.")

# Print the message 'The first three items in the list are:'. Then use a slice
# to print the first three items from that program's list.

print("The first three items in the list are:", animals[0:3])     # or print(animals[:3])

# Print the message 'Three items from the middle of the list are:'. Use a slice
# to print three items from the middle of the list.

print("Three items in the middle of the list are:", animals[1:4])

# Print the message 'The last three items from the middle of the list are:'
# and use a slice

print("The last three items in the list are:", animals[-3:])