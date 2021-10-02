# Lists and Strings

# This pattern is how to read a line, break into pieces, and then look at each word

# .split() splits a string and puts the values in a list
# these are now words
# we can access a particular word, or loop through all the words
abc = 'With three words'
stuff = abc.split()
print('abc:', abc)
print('after stuff = abc.split() ... stuff:', stuff)
print('len(stuff):', len(stuff))
print('stuff[0]:', stuff[0])

print('for w in stuff : print(w)')
for w in stuff :
    print(w)

# if you do not specify a delimiter, multiple spaces are treated like one delimeter
line = 'A lot        of spaces'
print('line:', line)
etc = line.split()
print('etc = line.split() gives:', etc)
print('.split() will count many spaces in a row as one space')

line = 'first;second;third'
thing = line.split()            # .split() counts spaces so this will split into one element
print('line:', line)
print('line.split()', thing, 'the length of this list is:', len(thing))
thing = line.split(';')         # this sets the delimiter to ';' so we get three elements
print('line.split(;)', thing, 'the length of this list is:', len(thing))

# double split pattern
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
print('line =', line)
words = line.split()
print('words = line.split() =', words)
email = words[1]
print('email = words[1] =', email)
email_pieces = words[1].split('@')
print("email_pieces = words[1].split('@')", email_pieces)
print('email_pieces[0] = username =', email_pieces[0])
print('email_pieces[1] = host name =', email_pieces[1])