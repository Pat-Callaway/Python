import sys
from pathlib import Path
import os # Importing the os module to create a folder
import logging
from os.path import isfile, join
from pathvalidate import sanitize_filename # pathvalidate installed via pip
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



def action_list():
    print("Which actions would you like to perform in the current directory?\n")
    print("1. Rename folder/file\n2. Move folder/file\n3. Copy folder/file\n4. Delete folder/file\n5. Navigate to a different directory\n")

    choice = input(">> ")


    match choice:

        case "1":
            logger.info(f"User selected {choice}")
            print("Which file or folder would you like to rename?")
            choice = input(">> ")
            clean_choice = Path(choice).expanduser().resolve()
            logger.info("sanitized user input...")


            if clean_choice.is_dir():
                new_name = clean_choice.rename(input("What would you like to rename the folder?\n>> "))
                logger.info(f"Attempting to change folder name..")
                new_folder = sanitize_filename(new_name)
                logger.info("Attempting to remove Illegal characters...")
                print(f"Folder successfully renamed to {new_folder}\n")
                logger.info(f"Folder was successfully renamed!")
                print(f"You are currently in {os.getcwd()}\n")
            if clean_choice.is_file():
                new_name = clean_choice.rename(input("What would you like to rename the file?\n>> "))
                logger.info("Attempting to change folder name...")
                new_file = sanitize_filename(new_name)
                logger.info("Attempting to remove illegal characters...")
                print(f"File successfully renamed to {new_file}\n")
                logger.info("File was successfully renamed!")
                print(f"You are currently in {os.getcwd()}\n")














def show_menu(): # User-defined function to reprompt user when navigating to different directory
    while True:
        print("What would you like to do?")
        print("1. List directories?\n2. List files?\n3. Navigate to a specific folder/file?\n4. Press 'q' to quit...")
        print("Please chose 1, 2, or 3...\n")

        logger.info("Awaiting user input")
        choice = input(">> ")

        if choice == "1":
            logger.info(f"User chose {choice}")
            print(os.listdir())
            logger.info("Successfully printed directories/folders...")
            action_list()
        elif choice == "2":
            logger.info(f"User chose {choice}")
            logger.info("Attempting to list all files in current directory")
            only_files = [f for f in os.listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
            print(only_files)
            logger.info("Successfully printed all files in current directory.")
            action_list()
        elif choice == "3":
            logger.info(f"User chose {choice}")
            print("Please type which folder/file you would like to open")
            new_directory = input(">> ")
            logger.info(f"Attempting to sanitize {new_directory} ")
            clean_new_directory = Path(new_directory).expanduser().resolve()  # Always make sure to sanitize user input
            if clean_new_directory.is_dir():
                os.chdir(clean_new_directory)
                logger.info("Successfully changed directories")
                print(f"You are now in {clean_new_directory}")
                # TODO: Add modules for safe functions and destructive functions
                action_list()
            elif clean_new_directory.is_file():
                with clean_new_directory.open("r") as file:
                    content = file.read()
                    print(content)
            else:
                logger.warning("Path does not exist")
                print("Please enter a valid path.")
                logger.info(f"Opening {clean_new_directory}...")
        elif choice == "q":
            logger.info("User quit program, closing application")
            sys.exit()
        else:
            print("Please enter a valid option")
            logger.error(f"User chose invalid option of {choice}")
            logger.info("Prompting user again...")


def main ():
    print("Which directory would you like to work in?")

    logger.info("Obtaining user input")

    while True: # while True is ALWAYS True
        user_input = input(">> ")
        clean_path = Path(user_input).expanduser().resolve()
        logger.info("sanitizing user input for directory")
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

    show_menu()

if __name__ == "__main__":
    main()





















"""""
for items in folder.glob("**/*"):
    if items.is_file():
        ext = items.suffix # This grabs the file's extension and assigns it to the variable ext
        files[ext] = files.get(ext, 0) + 1 # Gets the number of files with the same extension the .get() method returns the value if the key exists, otherwise it returns None
"""


















