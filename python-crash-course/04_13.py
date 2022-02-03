# Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.

buffet_foods = ('chicken', 'mashed potatos', 'chicken wings', 'corn', 'desserts')

# Use a for loop to print each food the restaurant offers

print("The menu for today is:")
for food in buffet_foods:
    print(food)

# Try to modify one of the items, and make sure that Python rejects the change

# buffet_foods[1] = ('green beans')

# Python returned TypeError

# The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu

buffet_foods = ('shredded pork', 'mashed potatos', 'chicken wings', 'corn', 'rolls')
print("The new menu for today is:")
for food in buffet_foods:
    print(food)