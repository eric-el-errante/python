message = "Hello Python world!"
print(message)
# 'message' is a variable and "Hello Python World!" is it's value, which is the information associated with that value

message = "Hello Python Crash Course world!"
print(message)
# this changes the value of 'message'

# variable names should be descriptive but short, for now just lowercase
# can begin with letter or underscore_, and can include numbers, but not as first characters
# obviously do not use reserved Python words like print, while

# print(mesage)
# this will create an error that Python will help you find
# in this case, that the variable 'mesage' is not defined because it is misspelled

# Strings are a series of characters. You can use either "" or '', allowing some flexibility
string1 = "This is a string."
string2 = 'This is also a string.'
string3 = 'I told my friend, "Python is my favorite language!"'
string4 = "The language of 'Python' is named after Monty Python, not the snake."
print(string1)
print(string2)
print(string3)
print(string4)

# Changing the case in a string. You can use methods. .title() runs the method on the variable 'name'. print() calls the function
# title() method changes the first letter of each word in a strong to a capital letter
# the () are emtpy because this method does not need any additional information
name = "ada Lovelace"
print(name)
print(name.title())
# upper() changes all letters in a string to uppercase
# lower() changes all letters in a string to lowercase
print(name.upper())
print(name.lower())

# using f-strings (format-strings) to combine strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
# The {} replace the variable name with it's value to use inside a string

# You can then assign a variable to a complete string if you want
message = f"Hello, {full_name.title()}!"
print(message)
# This makes the final print call easier to read, but it's essentially the same thing

# This is the old way of doing it, which the f-strings seem better to me
# here, the braces are filled with the variables listed in the ()
full_name = "{} {}".format(first_name, last_name)
print(full_name)
print(" ")

# \t will add in a tab
print("\tPython")
# \n adds a newline
print("Languages:\nPython\nJava\nHTML")
# you can combine these
print("Languages:\n\tPython\n\tJavacript\n\tHTML")
print(" ")

# removing 'whitespace', that is blank spaces to the left/right edge of a string
# use the method rstrip() or lstrip()
# strip() removes from both the left and right side simultaneously
# these are mainly used to clean up erroneous user input
favorite_language = "python "
other_language = "   HTML"
print(favorite_language)
print(other_language)
favorite_language = favorite_language.rstrip()
other_language = other_language.lstrip()
print(favorite_language)
print(other_language)