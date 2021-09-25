# If a number is entered, it will set the ival to an integer value
# which will then trigger the true portion of the if statement
# If a non-number is entered, it will set the ival to -1
# which will then trigger the else portion of the if statement

# This is good because no traceback will occur
# The program will run

rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Yes, that is a number.')
else:
    print('That is not a number.')