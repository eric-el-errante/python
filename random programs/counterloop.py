# Counting the amount of loops
# 'count' is a counter variable that starts at zero
# 1 is added to it each loop, which counts the # of loops

count = 0
print('The count at the start of the loop is:', count)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    print('Loop number is:', count, 'Value in set is:', value)
print('The count at the end of the loop is:', count)