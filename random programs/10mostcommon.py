fhand = open('romeo.txt')                           # opens file
counts = dict()                                     # creates blank dictionary

for line in fhand :
    words = line.split()                            # splits each line in the file into single strings
    for word in words :                             # loop through each word in each line
        counts[word] = counts.get(word, 0) + 1      # sets the key for the dictionary, and starts the count

# at this point we have created a dictionary with the word as the key,
# and the number of times it appears as the value

lst = list()                                        # creates blank list
for key, val in counts.items() :                    # starts going through each dictionary entry
    newtup = (val, key)                             # creates a tuple with the values first, keys second
    lst.append(newtup)                              # appends the values to the tuple
# print( sorted( [ (v, k) for k, v in counts.items() ] ) )
# another way to print the last block

lst = sorted(lst, reverse=True)                     # sorts lst from highest to lowest

for val, key in lst[:10] :                          # goes through the list for the first 10 entries
    print(key, val)                                 # prints the key, then the value