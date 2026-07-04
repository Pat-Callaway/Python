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
        case "2":
            logger.info(f"User selected choice {choice}")
            new_input = input("Which file or folder would you like to move? >\n")
            new_path = input("Which directory would you like to move the file or folder to? >>\n" )
            new_name = sanitize_filename(Path(new_input))
            new_path_dst = sanitize_filename(Path(new_path))

            if new_path_dst.is_dir():
                shutil.move(new_name, new_path_dst)
                print("Item has been successfully moved!")
                print(os.listdir(new_path_dst))
            else:
                logger.error("Invalid Path, item not moved")
                print("No such directory exists, please check your path")







def show_menu():  # User-defined function to reprompt user when navigating to different directory
    while True:

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
        elif choice == "3":
            logger.info(f"User chose {choice}")
            print("Please type which folder/file you would like to open")
            new_directory = input(">> ")
            logger.info(f"Attempting to sanitize {new_directory} ")
            clean_new_directory = Path(new_directory).expanduser().resolve()  # Always make sure to sanitize user input
            if clean_new_directory.is_dir():
                os.chdir(clean_new_directory)
                logger.info("Successfully changed directories")
                print(f"You are now in {clean_new_directory}\n")
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
            print("Closing application. Goodbye!")
            sys.exit()
        else:
            print("Please enter a valid option")
            logger.error(f"User chose invalid option of {choice}")
            logger.info("Prompting user again...")






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


