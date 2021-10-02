# user enters a filename and it is opened and read
# blank dictionary created
# for loop to read each line, split it, grab the email value
# and then make key/value pairs for each email
# loop to find the maximum number in the dictionary

fname = input('Enter file name: ')
fh = open(fname)
counts = dict()

for line in fh :
    line = line.rstrip()
    if line.startswith('From ') :
        newline = line.split()
        email = newline[1]
        counts[email] = counts.get(email, 0) + 1

bigword = None
bigcount = None
for word,count in counts.items() :
    if bigcount is None or count > bigcount :
        bigcount = count
        bigword = word
print(bigword,bigcount)