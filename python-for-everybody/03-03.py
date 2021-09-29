grade = input('Please enter your score between 0.0 and 1.0: ')
try :
    fgrade = float(grade)
except :
    print('That is not a number. Sorry!')
    quit()
if fgrade < 0.0 :
    print('That number is out of range. Sorry!')
elif fgrade < 0.6 :
    print('Your grade is an F.')
elif fgrade < 0.7 :
    print('Your grade is a D.')
elif fgrade < 0.8 :
    print('Your grade is a C.')
elif fgrade < 0.9 :
    print('Your grade is a B.')
elif fgrade <= 1.0 :
    print('Your grade is an A.')
else :
    print('That number is out of range. Sorry!')