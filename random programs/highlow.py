# This program will find the highest and lowest #'s in a set
# It's a bit of a cop-out with the initial values for big and
# small, but it works for now

values = [83, 43, 57, 11, 3, 45, 43]
big = -1
small = 101
for i in values :
    if i > big :
        big = i
    if i < small :
        small = i
print(big)
print(small)