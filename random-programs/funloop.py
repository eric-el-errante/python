count = 0
total = 0.0
while True :    # Loop will run until a 'break' is encountered
    value = input('Enter a number. Enter "done" when finished.')
    if value == 'done' :
        break   # sets the exit from the loop
    try :       # ensures only numbers are entered
        fvalue = float(value)
    except:
        print('Invalid input. Please enter a number.')
        continue # continues the loop to the next iteration
    count = count + 1
    total = total + fvalue
print('The total is:', total)
print('The amount of numbers entered is:', count)
try :           # ensure there is no zero division
    print('The average of entered numbers is:', total/count)
except :
    print('There is no average because you did not enter any numbers.')

# Could also just do a if/elif statement checking if count==0
