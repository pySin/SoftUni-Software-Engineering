# Delete File
import os


def delete_file():
    FOLDER_PATH = os.getcwd()
    FILE_NAME = "my_first_file.txt"
    FULL_PATH = os.path.join(FOLDER_PATH, FILE_NAME)
    try:
        os.remove(FULL_PATH)
    except FileNotFoundError:
        print("File already deleted!")


def call_functions():
    delete_file()


if __name__ == "__main__":
    call_functions()
