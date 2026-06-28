from pathlib import Path


# Testing to see if I can build this on my own with minimal help

files = {} # This creates an empty dictionary
lines = [] # This creates an empty list

# Opens the file in read mode
open("information.txt", "r")

"""""
The below code is to read the file line by line. Using the .stip() method to remove all the newline characters and spaces
This helps to make the code more readable. In information.txt the formatting is off and there are random newlines and spaces
which makes it difficult to read.

"""""
for line in open("information.txt", "r"):
    print(line.strip())