# Working with files
from builtins import print
from pathlib import Path

# Testing Pycharm and Python
# Run on command line - python app.py
# Add an empty list to store the lines
lines = []

folder = Path(r"*") # "." means the current directory
for file in folder.rglob("**/*"):
    print(file)
    lines.append(file) # adds the items into the list called lines
    print(file.name)
    print(file.suffix)
    print(file.is_file())






