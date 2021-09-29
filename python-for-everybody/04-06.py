def computepay(h,r) :
    if h <= 40 :
        total = h * r
    else :
        total = 40 * r + (h - 40) * r *1.5
    rtotal = round(total,2)
    return rtotal

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
actualpay = computepay(ihours,irate)
print('Pay:', actualpay)