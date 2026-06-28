# Working with files
from builtins import print

# Testing Pycharm and Python
# Run on command line - python app.py

with open("notes.txt") as f:
    contents = f.read()

print(contents)