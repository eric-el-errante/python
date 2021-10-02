# user enters a file
# finds lines that start with 'X-DSPAM-Confidence'
# isolates the number from those lines
# calculates the average of those numbers

fname = input('Enter file name: ')
fh = open(fname)
count = 0
total = 0
for line in fh :
    if not line.startswith('X-DSPAM-Confidence') :
        continue
    index1 = line.find(" ")
    strnum = line[index1 : ]
    str = strnum.strip()
    fstr = float(str)
    count = count + 1
    total = total + fstr
average = total / count
print('Average spam confidence:', average)