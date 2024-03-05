# File Reader
import os


def read_calculate():
    directory_path = os.getcwd()
    path = os.path.join(directory_path, "numbers.txt")
    file = open(path, "r")

    sum_numbers = 0
    for line in file:
        sum_numbers += int(line.strip("\n"))
    file.close()
    return sum_numbers


def call_functions():
    sum_numbers = read_calculate()
    print(sum_numbers)


if __name__ == "__main__":
    call_functions()
