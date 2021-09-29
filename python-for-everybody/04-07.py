def computegrade(score) :
    if score < 0.0 :
        print('That number is out of range. Sorry!')
        quit()
    elif score < 0.6 :
        letter = 'F'
    elif score < 0.7 :
        letter = 'D'
    elif score < 0.8 :
        letter = 'C'
    elif score < 0.9 :
        letter = 'B'
    elif score <= 1.0 :
        letter = 'A'
    else :
        print('That number is out of range. Sorry!')
        quit()
    return letter

grade = input('Please enter your score between 0.0 and 1.0: ')
try :
    fgrade = float(grade)
except :
    print('That is not a number. Sorry!')
    quit()
actualgrade = computegrade(fgrade)
print('Your score of', fgrade, 'is:', actualgrade)