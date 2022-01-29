# One Million: make a list of the numbers from one to one million, and then use
# a for loop to print the numbers. (If the output is taking too long, stop it
# by pressing CTRL-C or by closing the output window.)

numbers = []
for number in range(1,1000001):
    numbers.append(number)
for number in numbers:
    print(number)