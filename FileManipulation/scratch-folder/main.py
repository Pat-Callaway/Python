from itertools import count
from pathlib import Path
import os # Importing the os module to create a folder
import logging

# CREATES THE ACTUAL LOGGER
logger = logging.getLogger('logging_tool')
logger.setLevel(logging.DEBUG)
# CREATES FILE HANDLER
fh = logging.FileHandler('main.log')
# Set separate level for the file handler
fh.setLevel(logging.DEBUG)
# CREATES FORMATTER
formatter = logging.Formatter('%(asctime)s = %(name)s-%(levelname)s-%(message)s')
# ATTACHES FORMATTER
fh.setFormatter(formatter)
logger.addHandler(fh)
# Testing to see if I can build this on my own with minimal help

# files = {} # This creates an empty dictionary
# lines = [] # This creates an empty list

# Opens the file in read mode
 # open("information.txt", "r")


"""""
The below code is to read the file line by line. Using the .stip() method to remove all the newline characters and spaces
This helps to make the code more readable. In information.txt the formatting is off and there are random newlines and spaces
which makes it difficult to read.

"""""
"""""
folder = Path(r"D:\personal\downloads")

for file in folder.glob("**/*"):
    if file.is_file():
        ext = file.suffix
        files[ext] = files.get(ext, 0) + 1
# the above code is to count the number of files with the same extension
# using the .items() method to get the key and value
for ext, count in files.items():
    print(f"{ext}: {count}")
"""

"""""
Now that we have the key and value pairs, we can use the .get() method to get the value of the key.
"""""

# Creating folders to organize the files
# use os.mkdir() to create a folder
user_path = input("Please enter the path where you want your folder to be located: ")
user_folder = input("Please enter the name of the folder you wish to create: ")












