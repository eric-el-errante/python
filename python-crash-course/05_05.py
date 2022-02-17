# Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an
# if-elif-else chain.

alien_color = 'yellow'

# If the alien is green, player earned 5 points
# If the aline is yellow, player earned 10 points
# If the alien is red, player earned 15 points

if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
else:
    points = 15

print("You killed a", alien_color, "alien and earned", str(points), "points.")

# Write three version of this program, making sure each message is
# printed for the appropriate color alien.

alien_color = 'green'

if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
else:
    points = 15

print("You killed a", alien_color, "alien and earned", str(points), "points.")

alien_color = 'red'

if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
else:
    points = 15

print("You killed a", alien_color, "alien and earned", str(points), "points.")