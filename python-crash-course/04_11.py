# My Pizzas, Your Pizzas: Start with your proram from Exercise 4-1. Make a
# copy of the list of pizzas, and call it friend_pizzas. Then, do the following:

pizzas = ['pepperoni', 'sausuage', 'cheese']
friend_pizzas = pizzas

# Add a new pizza to the original list
pizzas.append('bacon')

# Add a different pizza to the list friend_pizzas
friend_pizzas.insert(1,'supreme')

# Prove that you have two separate lists. Print the message 'My favorite pizzas
# are:' and then use a for loop to print the first list. Do the same for your
# friends list.

for pizza in pizzas:
    print("My favorite pizzas are:", pizza)
for pizza in friend_pizzas:
    print("My friends favorite pizzas are:", pizza)
