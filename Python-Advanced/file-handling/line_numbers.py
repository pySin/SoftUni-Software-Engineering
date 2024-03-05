# Line Numbers


def lines_to_list() -> list:
    with open("text.txt", "r") as f:
        lines_list = f.readlines()
    return lines_list


def line_count(lines_list: list):
    for line_number, line in enumerate(lines_list):
        letter_count = len([letter for letter in line if letter.isalpha()])
        punctuation = "-,.?!'"
        punctuation_count = len([letter for letter in line if letter in punctuation])
        line = line.strip("\n")
        new_line = f"Line {line_number + 1}: {line} ({letter_count})({punctuation_count})"
        with open("output.txt", "a") as f:
            f.write(new_line + "\n")


def call_functions():
    lines_list = lines_to_list()
    line_count(lines_list)


if __name__ == "__main__":
    call_functions()
