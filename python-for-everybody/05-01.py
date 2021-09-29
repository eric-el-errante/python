total = 0
count = 0
while True :
    number = input('Please enter a number. Enter "done" to finish: ')
    if number == 'done' :
        break
    try :
        fnumber = float(number)
    except :
        print("Invalid input.")
        continue
    count = count + 1
    total = total + fnumber
print('Total is:',total)
print('Count is:',count)
if count != 0 : print('Average is:', total / count)