# 'message' is a variable, which is connected to a value
# in this case, message is the variable connected to the text value 
# 'Hello Python world!'
message = "Hello Python world!"
print(message)

# now you will see two lines of output
# it will print the text value of message, then message is re-assigned a new 
# text value and printed
message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)

# variable name rules:
    # contain letters, numbers, and underscores. They CANNOT start with a number
    # spaces are not allowed
    # do not use python keywords
    # make names short but descriptive

# This code would produce a traceback error, but the variable message is spelled
# incorrectly

    # message = "Hello Python Crash Course reader!"
    # print(mesage)

# Strings are series of characters, and you can use single or double quotes.
    # "This is a string."
    # 'This is also a string.'

# title() is a method, which performs an action on a piece of data. It is
# followed by a set of parentheses because you will usually have to add
# additional information for the method to use. So .title() tells Python to
# perform the method title() on the variable name. In this case, .title() makes
# each word in a string have title case, which capitalizes the first letter.
name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.upper()) # makes each character in a string uppercase
print(name.lower()) # makes each character in a string lowercase

# Combining string values. The {} tell Python to use the value of the variable.
# the f is an f-string (format-string) because Python formats the string by
# replacing the name of any variable with its value.
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

print(f"Hello, {full_name.title()}!")

# You can assign f-strings into variables
message = f"Hello, {full_name.title()}!"
print(message)

# Adding whitespace to format text
print("Python")
print("\tPython")   # \t will add a tab
print("Languages:\nPython\nC\nJava")    # \n will add a new line
print("Languages:\n\tPython\n\tC\n\tJava")

# stripping out whitespace to format text
# this is generally used to clean up user input
favorite_language = "Python "
print(favorite_language)
favorite_language = favorite_language.rstrip() # .rstrip() removes right whitespace
print(favorite_language)

favorite_language = " Python"
print(favorite_language)
favorite_language = favorite_language.lstrip() # .lstrip() removes left whitespace
print(favorite_language)

favorite_language = " Python "
print(favorite_language)
favorite_language = favorite_language.strip() # .strip() removes left/right whitespace
print(favorite_language)

# Integers can be added, subtracted, multiplied and divided
print('2+3 =',2+3)
print('2-3 =',2-3)
print('2*3 =',2*3)
print('2/3 =',2/3)

# Exponents use two asterisks
print('2^3 = 2**3 =',2**3)

# Floats are numbers with decimal points
print('0.1+0.1 =',0.1+0.1)
print('0.2+0.2 =',0.2+0.2)
print('2*0.1 =',2*0.1)
print('2*0.2 =',2*0.2)
print(0.2+0.1) # this will produce a number with a bunch of decimals, thats ok

# Division will always return a float, even it the result is a whole number
# Mixing integers and floats will always return a float
print('4/2=',4/2)
print('1+2.0=',1+2.0)

# You can use _ to visually group digits, doesn't matter where you put it
print('1000 = 1_000 = 10_00\n',1000,1_000,10_00)

# Multiple variable assignments can be done on the same line.
x, y, z = 0, 1, 2
print(x,y,z)

# Python does not have built-in constant types, but using all capital letters
# when assigning a variable name indicates it is a constant that should not
# be changed
PI = 3.141
print(PI)