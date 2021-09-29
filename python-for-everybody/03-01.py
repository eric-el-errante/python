hours = input('Enter hours: ')
rate = input('Enter rate: ')
ihours = float(hours)
irate = float(rate)
if ihours <= 40 :
    pay = ihours * irate
else :
    pay = 40 * irate + (ihours -40) * irate * 1.5
rpay = round(pay, 2)
print('Pay:',rpay)