# File Opener

def open_file():
    try:
        file = open("text.txt", "r")
    except FileNotFoundError:
        print("File not found")
    else:
        print("File found")


def call_functions():
    open_file()


if __name__ == "__main__":
    call_functions()
