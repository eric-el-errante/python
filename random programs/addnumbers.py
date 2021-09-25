# This takes user input for two numbers, then runs them through a
# function and returns the added value

a = input("Give me a number:")
b = input("Give me another number:")
a = int(a)
b = int(b)
def addtwo(aa,bb):
    added = aa + bb
    return added
print(addtwo(a,b))
