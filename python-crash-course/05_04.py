# Alien Colors #2: Choose a color for an alien as ou did in Exercise 5-3,
# and write an if-else chain.

alien_color = 'yellow'

# If the alien's color is green, print a statemtn that the player just
# earned 5 points for shooting the alien.
# If the alien's color isn't green, print a statement that the player just
# earned 10 points.

if alien_color == 'green':
    points = 5
else:
    points = 10

print("You just earned", str(points), "points.")

# Write one version of this program that runs the if block, and another
# that runs the else block.

alien_color = 'green'

if alien_color == 'green':
    points = 5
else:
    points = 10

print("You just earned", str(points), "points.")