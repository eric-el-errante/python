# Tuples are a more efficient, unmodifiable version of a list
# lists use brackets
# tuples use parenthesis

x = ('Alexis', 'Ryker', 'Indie')
print('x =', x)
print('x[2] =', x[2])
y = (1, 9, 2)
print('y =', y)
print('max(y) =', max(y))

for iter in y :
    print(iter)

# integer list is mutable
x = [9, 8 , 7]
x[2] = 6
print(x)

""""
# this will give a traceback, strings are immutable
y = 'ABC'
y[2] = 'D'
"""

""""
# this will give a traceback, tuples are immutable
z = (5, 4, 3)
z[2] = 0
"""

# things you can't do with tuples: sort, append, reverse

# things you can do with tuples: count, index
t = tuple()
print(dir(t))

# generally tuples are preferred over lists
# they do not have to be modifiable, so they are simpler and more efficient
# in terms of memory usage and performance

(x, y) = (4, 'eric')
print(y)
(a, b) = (99, 98)
print(a)

# tuples are comparable, starts comparing first elements, if equal moves to next
print('(0,1,2) < (5,1,2) =', (0,1,2) < (5,1,2))
print('(0,1,2000000) < (0,3,4)', (0,1,2000000) < (0,3,4))
print("('Jones','Sally') < ('Jones','Sam') = ", ('Jones','Sally') < ('Jones','Sam'))
print("('Jones','Sally') > ('Adams','Sam') = ", ('Jones','Sally') > ('Adams','Sam'))

# tuples are therefore sortable by the first element
d = {'a':10, 'b':1, 'c':22}
print(d.items())
print(sorted(d.items()))            # gives you back a sorted list of the dictionary items
# this is sorted based on the keys

# using sorted(), loops through dictionary in key order
d = {'a':10, 'b':1, 'c':22}
t = sorted(d.items())
print(t)
for k,v in sorted(d.items()) :
    print(k,v)

# how to sort by values instead of keys
c = {'a':10, 'b':1, 'c':22}             # creates a dictionary
tmp = list()                            # creates blank list
for k,v in c.items() :
    tmp.append((v,k))                   # goes through the dicionary tuples, amends it to the temp list in opposite order
print(tmp)
tmp = sorted(tmp)                       # sorts list by value
print(tmp)
tmp = sorted(tmp, reverse=True)         # sorts list in reverse order
print(tmp)

