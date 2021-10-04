# shit now we only have room for two guests!

guests = ['Richard Feynman', 'Albert Einstein', 'Carl Sagan', 'Galileo', 'Isaac Newton']
print(f'{guests[0]}, Would you like to come for dinner?')
print(f'{guests[1]}, Would you like to come for dinner?')
print(f'{guests[2]}, Would you like to come for dinner?')
print(f'{guests[3]}, Would you like to come for dinner?')
print(f'{guests[4]}, Would you like to come for dinner?')

print(f'{guests[2]} will not be able to attend.')
guests[2] = 'Werner Heisenberg'

print(f'{guests[2]}, Would you like to come for dinner?')

print('Guess what everyone? I found a bigger dining room table so I can invite more guests!')
guests.insert(0, 'Paul Dirac')
guests.insert(2, 'Briane Greene')
guests.append('Niels Bohr')

x = 0
while x < 8 :
    print(f'{guests[x]}, Would you like to come for dinner?')
    x = x + 1

print('Shit guys! Turns out the table will not make it here so we can only have two guests!')

x = 7
while x > 1 :
    popped_guest = guests.pop(x)
    print(f'Sorry, {popped_guest}, you will not be able to come to the dinner.')
    x = x - 1

print(f'{guests[0]} and {guests[1]}, you both can still attend the dinner.')

del guests[1]
del guests[0]

print(guests)