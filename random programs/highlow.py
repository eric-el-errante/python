# This program will find the highest and lowest #'s in a set
# It's assumed in this that all values in the set are positive
# None is like a place holder that holds a value
# By small = None we are basically saying we haven't seen a value
# and then our if statement is setting the first value we see
# as the smallest value
# professor put the big = -1, but to me makes sense to use None
# to compare both smallest and biggest
# -1 and None are flag values

big = -1
small = None
for value in [83, 43, 57, 11, 3, 45, 43] :
    if value > big :
        big = value
    if small is None :
        small = value
    elif value < small :
        small = value
print(big)
print(small)

biggest = None
smallest = None
for value in [83, 23, 54, 8, 777, 54, 0, -1, -14] :
    if biggest is None :
        biggest = value
    elif value > biggest :
        biggest = value
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
print(biggest)
print(smallest)