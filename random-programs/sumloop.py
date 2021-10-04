# Total a series of values
# 'total' is a sum variable that starts at zero and adds
# each value in the set to get a total sum

total = 0
print('The total at the start of the loop is:', total)
for value in [9, 41, 12, 3, 74, 15] :
    total = total + value
    print('The current total is:', total, 'The current value is:', value)
print('The total at the end of the loop is:', total)