# Using Functions, Store and Re-use

def thing():
    print('hello')
    print('fun')
thing()
print('zip')
thing()

# def DEFINES thing() as a 'variable' which when invoked should
# run the two print statements included
# it will NOT run when it is defined, only when invoked

# print() is a built-in function, int() is a built-in function, etc

def greet():
    return "Hello"

print(greet(), "Alexis")


# The return statement passes back a value
# In this example, i am passing two values to addtwo() and it
# returns one value, which is then assigned into x

def addtwo(a,b):
    added = a + b
    return added
x = addtwo(3,5)
print(x)

# fruitful functions return values
# non-fruitful functions do not return values