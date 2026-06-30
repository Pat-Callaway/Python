import sys
from pathlib import Path
import os # Importing the os module to create a folder
import logging
import shutil
from os.path import isfile, join

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

# Folder path for testing
print("Which directory would you like to work in?")

logger.info("Obtaining user input")


logger.info("sanitizing user input for directory")


while True: # while True is ALWAYS True
    user_input = input(">>")
    clean_path = Path(user_input).expanduser().resolve()
    logger.info(f"checking if {clean_path} is valid..")

    if clean_path.is_dir():
        logger.info("Valid directory found, changing directory")
        os.chdir(clean_path)
        print("You are now in " + os.getcwd())
        break
    else:
        logger.warning("Invalid path")
        print("Please enter a valid path...")

print()
print("What would you like to do?")
print("1. List directories?\n2. List files?\n3. Navigate to a specific folder/file?\n")
print("Please chose 1, 2, or 3...")

while True:
    user_input = input(">>")
    logger.info("Awaiting user input")

    if user_input == "1":
        print(os.listdir())
        logger.info("Successfully printed directories/folders...")
        break
    elif user_input == "2":
        logger.info("Attempting to list all files in current directory")
        only_files = [f for f in os.listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
        print(only_files)
        break


















"""""
for items in folder.glob("**/*"):
    if items.is_file():
        ext = items.suffix # This grabs the file's extension and assigns it to the variable ext
        files[ext] = files.get(ext, 0) + 1 # Gets the number of files with the same extension the .get() method returns the value if the key exists, otherwise it returns None
"""


















