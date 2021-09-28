"""
Reserved words in Python:
False   class   return    is      finally
None    if      for       lambda  continue
True    def     from      while   nonlocal
and     del     global    not     with
as      elif    try       or      yield
assert  else    import    pass    break
except  in      raise

Sentences or Lines
x = 2       Assignment Statement
x = x + 2   Assignment with Expression
print(x)    Print Function

x is a variable
=,+ are operators
2 is a constant
print() is a Function
"""

#Sequential Steps (this will print '2' and '4')
x=2
print(x)
x=x+2
print(x)

#Conditional Steps (this will print 'smaller than 10' and 'finish')
x=5
if x<10:
    print('Smaller than 10')
if x>20:
    print('Bigger than 20')
print('Finish')

#Repeated Steps (prints '5','4','3','2','1','Blastoff!')
n=5
while n>0:
    print(n)
    n=n-1
print('Blastoff!')
