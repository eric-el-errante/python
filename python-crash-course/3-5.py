# make a list of people you'd like to invite to dinner, then print each one
# a message. someone can't make it. add a print call at the end saying who
# cannot make it. replace the name of the person who can't make it, with the
# name of someone who can. 

guests = ['Richard Feynman', 'Albert Einstein', 'Carl Sagan', 'Galileo', 'Isaac Newton']
print(f'{guests[0]}, Would you like to come for dinner?')
print(f'{guests[1]}, Would you like to come for dinner?')
print(f'{guests[2]}, Would you like to come for dinner?')
print(f'{guests[3]}, Would you like to come for dinner?')
print(f'{guests[4]}, Would you like to come for dinner?')

print(f'{guests[2]} will not be able to attend.')
guests[2] = 'Werner Heisenberg'

print(f'{guests[2]}, Would you like to come for dinner?')
