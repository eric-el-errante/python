# Write a program to read through mbox-short.txt, and figure out the
# distribution of emails by hour.

fname = input('Enter file name: ')                     # asks user for input
fh = open(fname)                                       # opens the file

counts = dict()                                        # creates an empty dictionary
for line in fh :                                       # begins cycling through each line in the file
    line = line.rstrip()                               # strips the spaces from the right side
    if line.startswith('From ') :                      # looks for lines that start with 'From '
        newline = line.split()                         # splits the line starting with 'From ' into separate strings for each word
        time = newline[5]                              # turns the 6th value (time) in the line into a new string
        newtime = time.split(":")                      # splits the time string into hours, minutes and seconds by :
        hour = newtime[0]                              # hour is now the hour split from the time string
        counts[hour] = counts.get(hour, 0) + 1         # creates a dictionary with the hour # as the key, and the number of times as the value

for k, v in sorted(counts.items()) :                   # prints out the key/value in sorted order of counts 
    print(k, v)