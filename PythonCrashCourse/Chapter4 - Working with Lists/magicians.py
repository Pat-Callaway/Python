magicians = ['Hoodini', 'Copperfield', 'Angel', 'Blane']

# Using a for loop

for magician in magicians:
    print(magician)

# You can choose any name you want for the temporary variable, but it is useful to use a meaningful name that represents a single item from the list. See above.
# Indentation is crucial here, anything indented is in the loop body

# range() to generate a series of numbers

for value in range(1, 5):
    print(value)
# The above will print 1, 2, 3, 4. 1 in this example is inclusive and 5 is exclusive. Off-by-one behavior

# Creating a list of numbers with list() and range()

nums = list(range(101))
print(nums)

# Using steps

even_nums = list(range(2, 11, 2)) # Step is 2 - this is a list of numbers starting at 2 going to 10 incrementing by 2.
print(even_nums)

# More information in a for loop - adding the first 10 square numbers to an empty list

numbers = []
for value in range(11):
    number = value ** 2
    numbers.append(number)
print(numbers)

# min(), max(), sum()

digits = []
for value in range(20):
    print(value)

digits = [1, 2, 3, 4, 5]
print(min(digits)) # smallest element in list
print(max(digits)) # biggest element in list
print(sum(digits)) # sum of all elements in list

# List Comprehensions!! IMPORTANT

# Example

squares = [value**2 for value in range(11)] # Variable then operation, then for loop statement
print(squares)


