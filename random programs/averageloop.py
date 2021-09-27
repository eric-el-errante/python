# This loops calcalutes the average of values in a set
# It combines a sum loop and a counter loop to calculate
# the average of the set

count = 0
total = 0
print('The count at the start of the loop is:', count)
print('The total at the start of the loop is:', total)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    total = total + value
    print('Loop number is:', count, 'Value in set is:', value, 'Total is:', total, 'Average is:', total / count)
print('Average at the end of the loop is:', total / count)