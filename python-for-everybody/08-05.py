# open file mbox-short.txt and read it line by line
# look for lines starting with 'From' and not 'From:'
# parse the line using split() and print 2nd word in line
# then print out count at the end

fname = input('Enter file name: ')
fh = open(fname)
count = 0
for line in fh :
    line = line.rstrip()
    if line.startswith('From ') :
        newline = line.split()
        email = newline[1]
        print(email)
        count = count + 1
print("There were", count, "lines in the file with From as the first word")
