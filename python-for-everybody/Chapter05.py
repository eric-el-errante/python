# Loops and Iteration

# The while statement is like a for statement
# while is evaluating whether the comparision is true or false
# and runs WHILE the statement is true. Once the statement is no
# longer true it ceases to run.
n = 5
while n > 0 :
    print(n)
    n = n -1
print('Blastoff!')
print(n)
# n is an iteration variable that changes each time through a loop
# generally it will be a sequence of numbers

# Infinite loops will occur when there is no iteration variable
# or the iteration loop is improperly coded
# n = 5
# while n > 0 :
#     print('Lather')
#     print('Rinse')
# print('Dry off!')
# This code will run forever because n is ALWAYS going to be
# greater than 5. n is NOT changing!

# A zero trip loop will never run, because the initial
# statement is false
n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')

# How to get out of a loop with a break statement
# 'while True' is always true, so you must add in a break
# break is an 'escape the loop!'
while True :
    line = input('What is 5 + 4? ')
    line = int(line)
    if line == 9 :
        break
    print('Sorry! That is not correct. Please try again!')
print('Good job!')

# 'continue' ends the current iteration and jumps back
# to the the top of the loop and starts next iteration

while True :
    line = input('type a # sign first to continue without printing, or "done" to exit')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')

# so if you type a # sign first, it will go to 'continue' and
# then immediately return to the top of the loop instead of
# printing the input

# 'break' skips out of the loop
# 'continue" skips to the top of the loop

# Definite loops are finite loops 'for'

for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')
# i is the iteration value, it can be anything but i is standard

# doesn't have to be numbers in the set
friends = ['Alexis', 'Ryker', 'Indie']
for friend in friends :
    print('Hi there...', friend)
print('Done!')
# the set of 'friends' has 3 attributes, so the 'for' loop
# will run 3 times
# 'friend' is the iteration value
# 'friend' takes on the value 'Alexis', then 'Ryker', then 'Indie'

# Definite loops are for lines in a file, characters in a string,
# lists, etc. It will iterate through values in a set.

# Making smart loops!
# set some variables to initial values
# look for something or do something to each value in the set,
# which then updates a variable
# then look at the variables

# Counting the amount of loops
counter = 0
print('Before', counter)
for thing in [9, 41, 12, 3, 74, 15] :
    counter = counter + 1
    print(counter, thing)
print('After', counter)
# 'counter' is a counter variable that starts at zero

# Total a series of values
total = 0
print('Before', total)
for thing in [9, 41, 12, 3, 74, 15] :
    total = total + thing
    print(total, thing)
print('After', total)
# 'total' is a sum variable that starts at zero

# Finding the average
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    average = sum / count
    print(count, sum, value, average)
print('After', count, sum, sum / count)

# Filtering is looking for something that meets a criteria
# Putting an 'if' statement in a loop
print('Before')
for value in [9, 41, 12, 3, 74, 15] :
    if value > 20 :
        print ('Large number', value)
print('After')

# Search using a boolean value
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3 :
        found = True
    print(found, value)
print('After', found)
# All this is saying is that SOMEWHERE in the set we found a 3

# This 'is' and 'is not' operators are used in logical expressions
# it implies "is the same as", similar but strong than ==
# if smallest is None :
# if biggest is not True :
# is/not should be used for None/True/False, not for values