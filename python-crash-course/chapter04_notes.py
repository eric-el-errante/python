# for loops allow you to perform the same function on each element in a list,
# no matter how short of long the list

magicians = ['alice', 'david', 'carolina']  # defines a list
for magician in magicians:                  # pulls an element from the list, assigning it to a variable
    print(magician)                         # prints the current value of the variable

# the temporary variable can have any name, but it helps to make it associative
# for cat in cats:
# for dog in dogs:
# for item in list_of_items:

for magician in magicians:                  # pulls each element from the list
    print(f"{magician.title()}, that was a great trick!")   # print message using temp variable and applying title case
    print(f"I can't wait to see your next trick, {magician.title()}.")  # multiple lines can be in the for loop
print("Thank you, everyone. That was a great magic show!")  # this is NOT in the for loop

# using the range function to generate a series of numbers
# note that the final value in a range is NOT included
for value in range(1,5):
    print("Range(1,5):",value)
for value in range(1,6):
    print("Range(1,6):",value)

# using range() to make a list of numbers
numbers = list(range(1,6))  # a list has been made with the range function
print(numbers)

# the third argument in range() will cause a step
even_numbers = list(range(2,11,2))  # range goes from 2 to 10, skipping 2
print(even_numbers)

# playing with this
squares = []                    # creates an empty list
for value in range(1,11):       # creates a for loop for the given range
    square = value ** 2         # squares the number
    squares.append(square)      # add the squared number into the list
print(squares)                  # prints the list

# finding mins, maxs, and sums
digits = [1,2,3,4,5,6,7,8,9,0]
print("This is the list of digits:", digits)
print("The min(digits) is:", min(digits))
print("The max(digits) is:", max(digits))
print("The sum(digits) is:", sum(digits))

# list comprehension, this achieves the same thing 5 lines of code did
squares = [value**2 for value in range(1,11)]
print(squares)

# slicing a list, this will print various elements
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])     # prints the first 3 elements
print(players[:4])      # prints from the beginning to 4 elements
print(players[2:])      # prints from 3 element to end
print(players[1:3])     # prints from 2 to 4 element
print(players[-3:])     # prints from third from last to end

# looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on the team:")
for player in players[:3]:
    print(player.title())

# Copying a list, use an empty slide [:]
# This makes a slice which starts at first item and ends at last item
# effectively making a copy
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:", my_foods)
print("My friend's favorite foods are:",friend_foods)

# we can append an item to the end of each list to see they are in fact seperate
my_foods.append('canoli')
friend_foods.append('ice cream')
print("My favorite foods are:", my_foods)
print("My friend's favorite foods are:",friend_foods)

# THIS DOES NOT WORK
# friend_foods = my_foods will literally set friend_foods equal to my_foods
# thus any change make to either list will change the other list
