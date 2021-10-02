# open file romeo.txt and read line by line
# split each line into a list of words using .split()
# for each word on each line, check if the word is already in the list
# if not, add it to the list
# after that, sort the list alpabetically

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh :
    line = line.rstrip()
    newline = line.split()
    for x in newline :
        if x not in lst :
            lst.append(x)
lst.sort()
print(lst)