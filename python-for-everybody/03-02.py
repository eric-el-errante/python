hours = input('Enter hours: ')
try :
    ihours = float(hours)
except :
    print('Error, please enter numeric input.')
    quit()
rate = input('Enter rate: ')
try :
    irate = float(rate)
except :
    print('Error, please enter numeric input.')
    quit()
if ihours <= 40 :
    pay = ihours * irate
else :
    pay = 40 * irate + (ihours -40) * irate * 1.5
rpay = round(pay, 2)
print('Pay:',rpay)