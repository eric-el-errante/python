# Strings are a sequence of characters
# a string literal uses quotes 'Hello' or "Hello"
# for strings, + means "concatenate", which turns them into one string
# when a string is numbers, it's still a string
# convert nums in a string using int()

str1 = "Hello"
str2 = 'there'
bob = str1 + str2   # concatenates the strings
print(bob)

str3 = '123'
# x = str3 + 1     this will give a traceback, can't add num to a str
x = int(str3) + 1  # turns str into a num, can then add to it
print(x)

# it is preferable to read in data using strings, then prase and convert
# the data as we need, it gives us control over errors and bad input

# you can get any single character in a string using []
# it is the index value
# b a n a n a
# 0 1 2 3 4 5

fruit = 'banana'
letter = fruit[1]
print('The 2nd letter in "banana" is:',letter)
x = 3
w = fruit[x-1]
print(w)

# the len() function tells us the length of a string
print('The number of letters in "banana" is:',len(fruit))
a = 0
while a < len(fruit) :
    print(a, fruit[a])
    a = a + 1
# using a string as the set in a for/in loop makes each letter of the string
# the value in a set
# letter is the iteration variable, fruit is a six-character set (banana)
# so letter will take on each value in the set
for letter in fruit :
    print(letter)

# loop for finding numbers of 'a' in a word
word = 'banana'
print('This loop finds the number of times letter "a" is in:',word)
count = 0
for letter in word :
    if letter == 'a' :
        count = count + 1
print(count)

#slicing strings
# M o n t y   P y t h o  n
# 0 1 2 3 4 5 6 7 8 9 10 11
s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])
# start at low, but do not include high
print(s[:2])    # prints first two characters of string
print(s[8:])    # prints the 9th characters of string until end
print(s[:])     # prints whole string

fruit = 'banana'
if 'nan' in fruit :     # is the str 'nan' in the set of 'fruit'?
    print('Yes, there is an "nan" in', fruit)
else :
    print('No, there is not an "nan" in', fruit)

joke = 'team'
print('Is there an "i" in "team"?')
if 'i' in joke : print('There actually IS an "i" in team!')
else : print('No, there is no "i" in team')

# string comparison
worda = 'apple'
wordb = 'banana'
wordc = 'cupcake'
if worda == 'apple' : print(worda, '= apple')
if worda < wordb :
    print(worda,'comes before',wordb)
else :
    print(worda,'comes after', wordb)
if wordc > worda :
    print(wordc,'comes after',worda)
else :
    print(wordc,'comes before',worda)

#string library
greet = 'Hello Alexis'
lowercasegreet = greet.lower()
uppercasegreet = greet.upper()
print(greet,lowercasegreet,uppercasegreet)
print('Hi there'.lower())

stuff = 'Hello World'
print(type(stuff))
print(dir(stuff))       # this lists all the methods you can apply ************
print(stuff.rjust(20))