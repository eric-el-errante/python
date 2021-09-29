import random

# .random() picks a random number 0 <= number < 1
for i in range(10) :
    x = random.random()
    print(x)

# .randint(low,high) picks a random integer low <= number <= high
print(random.randint(5,10))
print(random.randint(5,10))

# .choice(variable) picks a random number from a set of numbers
t = [1, 2, 3]
print(random.choice(t))
print(random.choice(t))
