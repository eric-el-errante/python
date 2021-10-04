while True :
    num = input('Please enter a number: ')
    try :
        inum = int(num)
    except :
        print('That is not a valid number. Sorry!')
        break
    if inum%2 == 0 :
        print('The number is even.')
        continue
    else :
        print('The number is odd.')
    continue
    if num == 'done' :
        break