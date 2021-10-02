# Dictionaries and Files

counts = dict()                                 # creates a dictionary
print('Enter a line of text:')                  # prompts user for input
line = input('')                                # assigns input string to a variable

words = line.split()                            # splits the string into a list

print('Words:', words)                          # prints the list

print('Counting...')
for word in words :
    counts[word] = counts.get(word, 0) + 1      # counts the words and assigns them into a dictionary
print('Counts', counts)

# the gist is to split a line into words
# loop through the words
# and use a dictionary to track the count of each word

for key in counts :
    print(key, counts[key])
# it will iterate through the keys, but you can also get the value

# retrieving lists of keys and values
jjj = {'alexis': 1, 'ryker': 42, 'indie': 100}
print(list(jjj))        # list of keys
print(jjj.keys())       # list of keys
print(jjj.values())     # list of values
print(jjj.items())      # list of values/keys

# two iteration variables!
# aaa goes through the keys
# bbb goes through the values
for aaa,bbb in jjj.items() :
    print(aaa,bbb)

# bringing it all back together
name = input('Enter file:')                     # gets input from user
handle = open(name)                             # opens file to read

counts = dict()                                 # creates dict
for line in handle :                            # goes through each line in the file
    words = line.split()                        # splits linestring into a list of words
    for word in words :                         # goes through each word after split
        counts[word] = counts.get(word, 0) + 1  # assigns key/value pairs into dictionary counting

bigcount = None                                 # default values for counting
bigword = None
for word,count in counts.items() :              # begins iteration through the dict
    if bigcount is None or count > bigcount :   # checks though the values to see if it is greater than the last value
        bigword = word
        bigcount = count

print(bigword, bigcount)