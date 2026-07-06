names = ['Jin', 'Danny', 'Katie', 'Patrick', 'Phil', 'Skeletor', 'Jonesy']


# Getting names by index position

print(names[0])

print(f"Hello, {names[4].title()}! How are are you today?")
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])
print(names[6])

# Modifying the list to add an element at index 0, index 0 now Scooby rather than Jin.

names[0] = 'Scooby'
print(names)

# Adding (appending) elements to a list

names.append('Sam')
print(names)

empty_list = [] # Creates an empty list

empty_list.append('One')
empty_list.append('Two')
empty_list.append('Three')

print(empty_list)

empty_list.insert(2, 'Four') # Specify the index first, then the object
print(empty_list)

# If you know the index of what item you want to remove from the list use del
del empty_list[3]

print(empty_list)

# using pop() - let's you remove the last item from a list, but you can still work with it
popped_list = empty_list.pop()
print(empty_list)
print(popped_list)