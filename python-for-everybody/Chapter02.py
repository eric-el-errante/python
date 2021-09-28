# Variable Name Rules
# must start with letter or underscore_, can have numbers too
# Case sensitive

""""
+   Addition
-   Subtraction
*   Multiplication
/   Division
**  Power
%   Remainder (modulus)
//  Division but will truncate the decimal portion

"""

# Integer Division will results in a floating point result

# User Input
nam=input("Who are you?")
# the input() function pauses and waits for user input, and will return a string
print('Welcome',nam)
# inam=int(nam) will turn the string value of nam into an integer if a number is the expected input

x = 5343432
print(x)
print(x % 10)
print(x % 100)