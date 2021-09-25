# Conditional Steps
# Common to indent 4 spaces, better to use 4 spaces rather than tab
x=5
if x<10:
    print('Smaller')
if x>20:
    print('Bigger')
print('Finis')

"""
Comparison Operators
<   Less than
<=  Less than or Equal to
==  Equal to
>=  Greater than or Equal to
>   Greater than
!=  Not equal
"""
x=5
print('x=',5)
if x==5:
    print(x,'Equal 5')
if x>4:
    print(x,'greater than 4')
if x>=5:
    print(x,"greater than or equal to 5")
if x<6: print(x,'less than 6')                  # you can put this part on the same line instead of indenting,which is syntax
if x <=5: print(x,'less than or equal 5')
if x!=6:
    print(x,'not equal 6')

# Example of longer indented block, all the indented portions are "contained" within the if statement
x=5
print('Before 5')
if x==5:
    print('Is 5')
    print('Is still 5')
    print('Third 5')
print('Afterwards 5')

# Nested Decision
x=42
if x>1:
    print('More than one')
    if x<100:
        print("Less than 100")
print('all done')

# Two-way Decisions....for-else
x=2
if x>2:
    print('Bigger')
else:
    print('Smaller')
print('all done')