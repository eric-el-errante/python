# Algorithms are a set of rules/steps to solve a problem
# Data Structures are a particular way of organizing data in a computer

# so far out variables have had one value in them, the value of which is 
# overriden when we put in a new value

# a collection allows us to put many values in a single 'variable'
# convenient because we can carry many values in one package
# square brackets is a list constant

friends = ['Alexis','Ryker','Indie']
carryon = ['GPS Watch', 'Minimus shoes', 'Camera']
print(friends, carryon)
# friends/carryon are now a LIST OF STRINGS, not just one string

# lists can have different types in them
# they can be empty
print('red',24,98.6)
print([])

# lists can have other lists inside them
list1 = [1, [5,6],7]
print(list1)

# this was a list we already used with a for loop
# basically any for loop we have been using is using a list already
for i in [5,4,3,2,1] :
    print(i)
print('Blastoff!')

# friends is a set i.e. list
count = 0
print(friends)
for friend in friends :
    print(friend,'the sub value is:',count)
    count = count + 1

# strings are immutable, that cannot have contents changes
# must make a new string to make a change
# lists are mutable - we can change an element using the index operator
fruit = 'Banana'
# fruit[0] = 'b' this would cause a traceback because a string is immutable
# here we are making a change to the string but assigning it to a new variable
x = fruit.lower()
print(x)
lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28   # lotto is a list, so we can change values in it
print(lotto, 'changed value 26 to 28 using lotto[2] = 28')

print('Here is our list named "friends"',friends)
print('There are', len(friends), 'values in the list "friends"')

# len() will tell us the number of elements in a set/list
x = [1, 2, 'indix', 99]
print(len(x))

# range function returns a list of numbers that range from 0 to one less than parameter
# we can construct an index loop using 'for' and an integer iterator
print(range(4))
print(len(friends))
print(range(len(friends)))

# these two 'for' loops accomplish the same thing
# don't really understand the point of the integer interator yet
for friend in friends :
    print("What's up",friend,"?")
for i in range(len(friends)) :
    friend = friends[i]
    print(i)
    print("What's up",friend,'?')
# i guess for second we know what 'i' for each iteration of the loop
# seems like maybe it gets rid of the need for count = blah blah blah

# lists can be added / concatonated, order matters
a = [1,2,3]
b = [4,5,6]
c = a + b
d = b + a
print(a)
print(b)
print('a + b =', c)
print('b + a', d)

# lists can be sliced REMEMBER UP TO BUT NOT INCLUDING
t = [9, 41, 12, 3, 74, 15]
print('t =',t)
print('t[1:3] = ', t[1:3])
print('t[4] =', t[4])
print('t[3:] =', t[3:])
print('t[:] =', t[:])

# list methods
x = list()
print('x = list(), the type of x is: ',type(x))
print('methods that can be used with lists: ', dir(x))

# building a list from scratch
# .append() adds element to end of list
stuff = list()
print('the list stuff:', stuff)
stuff.append('book')
stuff.append(99)
print("after stuff.append('book') and stuff.append(99), the list stuff:",stuff)
stuff.append('cookie')
print("after stuff.append('cookie'), list is:", stuff)

# using 'in'
some = [1, 9, 21, 10, 16]
print(some, '9 in some...', 9 in some)
print(some, '15 in some...', 15 in some)
print(some, '20 not in some...', 20 not in some)
# this is a logical operator and does not modify the list

# lists can hold many items and its keeps those items in order unless we change it
friends = ['Alexis', 'Ryker', 'Indie', 'Eric']
print("'friends' in normal order:", friends)
friends.sort()                                      # this bit is kind of weird because you just run the method, it changes the list
print("'friends' after friends.sort()", friends)

# built-in functions and lists
nums = [3, 41, 12, 9, 74, 15]
print('nums list:', nums)
print('len(nums):', len(nums), 'is the number of elements in the list')
print('max(nums):', max(nums), 'is the maximum value of the elements in the list')
print('min(nums):', min(nums), 'is the minimum value of the elements in the list')
print('sum(nums):', sum(nums), 'is the sum of all the elements in the list')
print('sum(nums)/len(nums) i.e. average:', sum(nums)/len(nums), 'is an average of the elements in the list')
nums.sort()
print('now the list is sorted using nums.sort', nums)
# REMEMBER IF YOU RUN A METHOD ON A LIST IT CHANGES THE ORDER OF THE LIST!!!!

# two different ways to do the same thing, now with list methods compared to a 'for' loop
total = 0
count = 0
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average:', average)

numlist = list()
while True :
    inp = input('Enter a number:')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)               # since numlist is a blank list, .append() will add in values in order
average = sum(numlist) / len(numlist)
print('Average:', average)
print('our entered values have become a list:', numlist)
# they both seem fairly fine, but the benefit of the second way is that
# we have all the entered values in a list afterwards which is cool
# but, if you have a shit ton of numbers, the first way only keeps 1 number in memory
# the second way keeps ALL those numbers in memory
# also, if you already have numbers in a list, the 2nd way is obviously better