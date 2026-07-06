guests = ['Tyler Durden', 'Abraham Lincoln', 'Jack', 'Marla', 'Harrison', 'Kurt', 'Dean', 'Stacey', 'Danielle', 'Jackie', 'Donna']

# Oh no! some guests cannot make it to the party, let's adjust the list (Exercisse 3-5)

# The guest who can not make it is....
bailed_guest = guests.pop(5)

# Who am I going to invite now?


print(f"{bailed_guest} couldn't make it to the party! So they are out!\n")
print("So we have the following people coming, and I am inviting one more person!")
print(guests)
print("I am going to invite Lisa!")
guests.append('Lisa')
print("Here is the new list for the party!")
print(guests)

# sorting lists with sort()
guests.sort() # This changes the order of the list PERMANENTLY!
print(guests)

cars = ['audi', 'bmw', 'ford', 'chevy']
# Reverse sort with sort(reverse=True)
cars.sort(reverse=True) # Also changes order of the list permanently!!
print(cars)

# sorted() vs sort() - sorted() function maintains the original order of a list but PRESENT it in a sorted order.

sandwiches = ['BLT', 'Turkey', 'Ham', 'Tuna', 'Grilled Cheese']
print(sorted(sandwiches))
print('The above list is now sorted, but the original list is preserved at below...')
print(sandwiches)

# reverse() changes list permanently!!
sandwiches.reverse()
print(sandwiches)

# len() - Finding the length of a list!!
print(len(sandwiches))

