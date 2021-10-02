# Dictionaries, our second data structure, collection

# List is a linear collection of values that stay in order
# Dictionary is like a 'bag' of values, each with own label
    # it's like a baby database

purse = dict()

#      key       value
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
# the value is going into the dictionary with the label 'key'

print('print(purse) =',purse)
print("purse['candy'] =", purse['candy'])

# you can modify the values, mutable
purse['candy'] = purse['candy'] + 2
print(purse)

# Lists and Dictionary are very similar
# lists are ordered and dictionaries are not
# lists have positions, dictionaries have labels
""""
List                        Dictionary
lst = list()                ddd = dict()
lst.append(21)              ddd['age'] = 21
lst.append(183)             ddd['course'] = 182
>>>print(lst)               >>>print(ddd)
[21, 183]                   {'course': 182, 'age': 21}
lst[0] = 23                 ddd['age'] = 23
>>>print(lst)               >>>print(ddd)
[23, 183]                   {'course': 182, 'age': 23}
"""

# Dictionary literals (constants)
jjj = {'alexis': 1, 'ryker': 42, 'indie': 100}
print(jjj)
ooo = {}        # this is the same as ooo = dict()
print(ooo)

# doing a count with names and new names
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts :
        counts[name] = 1                  # creates a key/value pair if not already in dict
    else :
        counts[name] = counts[name] + 1   # adds 1 to the value if key is already in the dict
print(counts)

# 'get' method, not explained well, need help
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1    # the 0 is the default for new keys, otherwise name and then add 1
print(counts)


