# Files! Into the real world!
# open() returns a 'file handle' - variable to perform operations on the file
# handle = open('filename','mode') {mode - 'r'read 'w'write}

handle = open("words.txt", "r")
print(handle)

# this will print each line in the file
for cheese in handle :
    print(cheese)

# this will print out the number of lines in a file
count = 0
for cheese in handle :
    count = count + 1
print('Line Count:', count)