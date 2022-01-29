# Shrinking Guest List: You just found out that your new dinner table won't
# arrive in time for the dinner, and you have space for only two guests.

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

print("Well, now it turns out the table will not arrive in time.")
print("I can only invite two guests to the dinner.")
popped_guest = guest_list.pop()
print(f"Sorry, {popped_guest}, you can't come to dinner.")
popped_guest = guest_list.pop()
print(f"Sorry, {popped_guest}, you can't come to dinner.")
popped_guest = guest_list.pop()
print(f"Sorry, {popped_guest}, you can't come to dinner.")
popped_guest = guest_list.pop()
print(f"Sorry, {popped_guest}, you can't come to dinner.")

print(f"{guest_list[0]} and {guest_list[1]}, you are still invited to dinner.")
del guest_list[1]
del guest_list[0]
print(guest_list)