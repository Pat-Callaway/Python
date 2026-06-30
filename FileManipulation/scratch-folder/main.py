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

# Create an empty dictionary to hold key : value pairs
files = {}

# Folder path for testing
folder = Path(".")
for items in folder.glob("**/*"):
    logger.info("Scanning items")
    if items.is_file():
        ext = items.suffix # This grabs the file's extension and assigns it to the variable ext
        files[ext] = files.get(ext, 0) + 1 # Gets the number of files with the same extension the .get() method returns the value if the key exists, otherwise it returns None



















