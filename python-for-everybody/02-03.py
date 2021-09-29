hours = input('Enter hours: ')
rate = input('Enter rate: ')
ihours = float(hours)
irate = float(rate)
pay = ihours * irate
rpay = round(pay, 2)
print('Pay:',rpay)