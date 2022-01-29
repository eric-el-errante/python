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

