# Dinner Guest: Working with one of the programs from earlier, use len()
# to print a message indicating the number of people you are inviting to
# dinner

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

print(f"Hey, {guest_list[0]}, and {guest_list[1]}, and {guest_list[2]}, we found a bigger table!")
guest_list.insert(0,'Indie')
guest_list.insert(1,'Ryker')
guest_list.append('Mom')
print(f"{guest_list[0]}, would you like to come to my party?")
print(f"{guest_list[1]}, would you like to come to my party?")
print(f"{guest_list[2]}, would you like to come to my party?")
print(f"{guest_list[3]}, would you like to come to my party?")
print(f"{guest_list[4]}, would you like to come to my party?")
print(f"{guest_list[5]}, would you like to come to my party?")
print(guest_list)
print(f"I have invited {len(guest_list)} people to my party.")