# File Writer


def create_file():
    with open("my_first_file.txt", "w") as f:
        f.write("I just created my first file!")
    print(f.closed)


def call_functions():
    create_file()


if __name__ == "__main__":
    call_functions()
