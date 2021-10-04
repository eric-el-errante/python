# invite three more guests to dinner. 


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

