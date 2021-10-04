# use a variable to represent a person's name, and include whitespace
# characters at the beginning and end. use /t and /n as well.
# print the name with the whitespace, then print it after stripping the whitespace

name = '     \tAlexis\nHennecy   '
print('Name with whitespaces:\n', name)
print('Name with .lstrip() method:\n', name.lstrip())
print('Name with .rstrip() method:\n', name.rstrip())
print('Name with .strip() method:\n', name.strip())