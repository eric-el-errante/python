# if statements allow you to look for a specific circumstance and take
# action accordingly

from tkinter import EW


cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Conditional tests i.e. True or False
# if the statement is True, python will execute the code
# if the statement is False, python will not execute the code

car = 'bmw'
print(car == 'bmw')
print(car =='audi')

# Testing for equality is case-sensitive
car = 'Audi'
print(car == 'audi')
print(car.lower() == 'audi')

# != is not equal to

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# Checking numerical comparisions

age = 18
print(age == 18)

answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again.")

age = 19

print(age < 21, age <= 21, age > 21, age >= 21)

# Checking multiple conditions using and, all conditions must be True

age_0 = 21
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

# Checking multiple conditions using or, at least one condition must be True

age_0 = 22
age_1 = 18
print(age_0 >=21 or age_1 >= 21)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

# Checking for a value in a list

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

# Checking for value NOT in a list

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Boolean expression is either True or False
