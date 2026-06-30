# Working with files
from builtins import print
from pathlib import Path

# Testing Pycharm and Python
# Run on command line - python app.py
# Add an empty list to store the lines
file_extensions = {} # this is a dictionary


folder = Path(r"D:\personal\downloads") # "." means the current directory
for file in folder.glob("**/*"):
    if file.is_file():
        ext = file.suffix # Gets the file extension
        file_extensions[ext] = file_extensions.get(ext, 0) + 1 # Gets the number of files with the same extension the .get() method returns the value if the key exists, otherwise it returns None




# using the .items() method to get the key and value
# using an f string to mix variables into a string
for ext, count in file_extensions.items():
    print(f"{ext}: {count}")







