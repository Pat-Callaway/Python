# Working with files
from builtins import print
from pathlib import Path

# Testing Pycharm and Python
# Run on command line - python app.py
# Add an empty list to store the lines
lines = []

folder = Path(r"D:\personal\downloads") # "." means the current directory
for file in folder.glob("**/*"):
    if file.is_file():
        print(file.name, "is a file")
    else:
        print(file.name, "is a folder")







