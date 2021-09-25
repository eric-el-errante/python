# This assigns a letter grade based on a numeric input
# If a non-number is entered, it will display an error and quit
# If a number out of range is entered, it will display an error
# If a valid number is entered, it will display a letter grade

score = input("Enter your score:")
try:
    fscore = float(score)
except:
    print("Error: Invalid input, not a number")
    quit()
if fscore > 1.0:
    print("Error: Invalid Range")
elif fscore >= 0.9:
    print("A")
elif fscore >= 0.8:
    print("B")
elif fscore >= 0.7:
    print("C")
elif fscore >= 0.6:
    print("D")
elif fscore >= 0:
    print("F")
else:
    print("Error: Invalid Range")