# Files! Into the real world!
# open() returns a 'file handle' - variable to perform operations on the file
# handle = open('filename','mode') {mode - 'r'read 'w'write}

handle = open("sample3.txt", "r")
print(handle)

# this will print each line in the file
for cheese in handle :
    print(cheese)

# this will print out the number of lines in a file
count = 0
for cheese in handle :
    count = count + 1
print('Line Count:', count)

# this is supposed to read the whole thing into a string
# then print the amount of characters
# then print the start through the 21st character
inp = handle.read()
print(len(inp))
print(inp[:20])

# will look for lines that start with this phrase then print
for line in handle :
    if line.startswith('Quod') :
        print(line)

# same as above but strips out the new line
fhand = open('sample3.txt')
for line in fhand :
    line = line.rstrip()
    if line.startswith('Quod') :
        print(line)

# same as above, but skips lines instead of finds lines
# if line does NOT start with quod, it continues to next iteration
# if line does start with code it prints it
fhand = open('sample3.txt')
for line in fhand :
    line = line.rstrip()
    if not line.startswith('Quod') :
        continue
    print(line)

# looks for a string anywhere in a line, prints it, skips if not
fhand = open('sample3.txt')
for line in fhand :
    line = line.rstrip()
    if not 'est' in line :
        continue
    print(line)

# prompt for a filename
fname = input('Enter a file name: ')
fhand = open(fname)
count = 0
for line in fhand :
    if line.startswith('Quod') :
        count = count + 1
print('There were', count, 'lines that start with Quod')

# dealing with bad file names
fname = input('Enter a file name: ')
try :
    fhand = open(fname)
except :
    print('File cannot be opened.', fname)
    quit()
count = 0
for line in fhand :
    if line.startswith('Quod') :
        count = count + 1
print('There were',count,'lines starting with Quod in',fname)