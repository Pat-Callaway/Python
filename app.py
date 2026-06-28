# Working with files
from builtins import print

# Testing Pycharm and Python
# Run on command line - python app.py
# Add an empty list to store the lines
lines = []

with open("notes.txt") as f:
    for line in f:
        clean = line.strip().lower()
        # The line below adds the line to the list, now you can actually work with the data.
        lines.append(clean)
print(lines)

