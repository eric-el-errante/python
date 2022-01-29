# Changing Guest List: You just heard that one of your guests can't make
# the dinner, so you need to send out a new set of invitations. You'll have to
# think of someone else to invite.

guest_list = ['Alexis Hennecy', 'Richard Feynman', 'Brian Greene']
print(f"Hi there, {guest_list[0]}, would you like to come to my party?")
print(f"Hi there, {guest_list[1]}, would you like to come to my party?")
print(f"Hi there, {guest_list[2]}, would you like to come to my party?")

print(f"Unfortunately, {guest_list[1]} cannot make the party.")
del guest_list[1]
guest_list.append('Albert Einstein')
print(f"Hi there, {guest_list[0]}, would you like to come to my party?")
print(f"Hi there, {guest_list[1]}, would you like to come to my party?")
print(f"Hi there, {guest_list[2]}, would you like to come to my party?")