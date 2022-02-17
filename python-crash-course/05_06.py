# Stages of Life: Write an if-elif-else chain that determines a persons
# stage of life. Set a value for the variable age, and then:

age = 38

# If the person is less than 2 years old, print a message that the person
# is a baby

if age < 2:
    print("You are a baby.")

# If the person is at least 2 years old but less than 4, print a message
# that the person is a toddler

elif age < 4:
    print("You are a toddler.")

# If the person is at least 4 years old but less than 13, print a message
# that the person is a kid.

elif age < 13:
    print("You are a kid.")

# If the person is at least 13 but less than 20, print a message that the
# person is a teenager

elif age < 20:
    print("You are a teenager.")

# If the person is at least 20 but less than 65, print a message that the
# person is an adult

elif age < 65:
    print("You are an adult.")

# If the person is 65 or older, print a message that the person is an elder

else:
    print("You are an elder.")