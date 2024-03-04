# File Manipulator
import os


def create_file(file_name: str):
    with open(file_name, "w") as f:
        f.write("")


def add_content(file_name: str, content: str):
    with open(file_name, "a") as f:
        f.write(f"{content}\n")


def replace_string(file_name: str, old_string: str, new_string: str):
    try:
        with open(file_name, "r") as f:
            text = f.read()
            text = text.replace(old_string, new_string)
    except FileNotFoundError:
        print("An error occurred")
    else:
        with open(file_name, "w") as w_file:
            w_file.write(text)


def file_delete(file_name: str):
    try:
        directory_path = os.getcwd()
        full_path = os.path.join(directory_path, file_name)
        os.remove(full_path)
    except FileNotFoundError:
        print("An error occurred")


def call_functions():
    command = input()
    while command != "End":
        if command.startswith("Create"):
            instructions = command.split("-")
            file_name = instructions[1]
            create_file(file_name)
        elif command.startswith("Add"):
            instructions = command.split("-")
            file_name = instructions[1]
            content = instructions[2]
            add_content(file_name, content)
        elif command.startswith("Replace"):
            instructions = command.split("-")
            file_name = instructions[1]
            old_string = instructions[2]
            new_string = instructions[3]
            replace_string(file_name, old_string, new_string)
        elif command.startswith("Delete"):
            instructions = command.split("-")
            file_name = instructions[1]
            file_delete(file_name)

        command = input()


if __name__ == "__main__":
    call_functions()
