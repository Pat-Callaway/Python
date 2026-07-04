import sys
from pathlib import Path
import os  # Importing the os module to create a folder
import logging
from os.path import isfile, join
from pathvalidate import sanitize_filename  # pathvalidate installed via pip
import shutil

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

'''''
def action_list():
    print("Which actions would you like to perform in the current directory?\n")
    print(
        "1. Rename folder/file\n2. Move folder/file\n3. Copy folder/file\n4. Delete folder/file\n5. Navigate to a different directory\n")

    choice = input(">> ")

    match choice:

        case "1":
            logger.info(f"User selected {choice}")
            print("Which file or folder would you like to rename?")
            choice = input(">> ")
            clean_choice = Path(choice).expanduser().resolve()
            logger.info("sanitized user input...")

            if clean_choice.is_dir():
                new_input = input("What would you like to rename the folder?\n>> ")
                logger.info("Attempting to remove Illegal characters...")
                new_name = sanitize_filename(new_input)
                logger.info(f"Attempting to change folder name..")
                new_folder_name = clean_choice.rename(clean_choice.with_name(new_name))
                print(f"Folder successfully renamed to {new_folder_name}\n")
                logger.info(f"Folder was successfully renamed!")
                print(f"You are currently in {os.getcwd()}\n")
            elif clean_choice.is_file():
                new_input = input("What would you like to rename the file?\n>> ")
                logger.info("Attempting to remove Illegal characters")
                new_name = sanitize_filename(new_input)
                logger.info("Attempting to change file name...")
                new_file_name = clean_choice.rename(clean_choice.with_name(new_name))
                print(f"File successfully renamed to {new_file_name}\n")
                logger.info("File was successfully renamed!")
                print(f"You are currently in {os.getcwd()}\n")
            else:
                logger.warning("Valid path not provided...")
                print("No such folder or file found...")
'''''



def show_menu():  # User-defined function to reprompt user when navigating to different directory
    while True:

        print("1. List directories?\n2. List files?\n3. Navigate to a specific folder/file?\n4. Press 'q' to quit...")
        print("Please chose 1, 2, or 3...\n")

        logger.info("Awaiting user input")
        choice = input(">> ")






def main():
    logger.info("Starting program...")
    print("Welcome to File Cleaner\n")
    print("You will be able to chose to navigate your system and modify folders and files.\n")
    starting_directory = Path('C:\\Users\\')
    os.chdir(starting_directory)

    print(f"You are currently in {os.getcwd()}\n")
    print("What would you like to do?")

    show_menu()



if __name__ == "__main__":
    main()


