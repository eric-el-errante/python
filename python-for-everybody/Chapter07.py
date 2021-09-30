# Files! Into the real world!
# open() returns a 'file handle' - variable to perform operations on the file
# handle = open('filename','mode') {mode - 'r'read 'w'write}

handle = open("words.txt", "r")
print(handle)