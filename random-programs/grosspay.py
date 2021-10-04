# This will print out gross pay depending on hours worked
# If non-numeric values are input for the hours or rate
# it will print an error message and then quit

sh = input("Enter your hours: ")
sr = input("Enter your pay rate: ")

try:
    fh = float(sh)
    fr = float(sr)
except:
    print("error: please enter numeric input")
    quit()

if fh > 40:
    reg = fr * fh
    otp = (fh - 40) * (fr * .5)
    xp = reg + otp
else:
    xp = fh * fr

print("Pay:", xp)