# Treasure Finder


def display_data(word_positions):

    type_slice = []
    coordinate_slice = []

    for i in range(len(word_positions)):
        if word_positions[i] == "&":
            type_slice.append(i)
        elif word_positions[i] in "<>":
            coordinate_slice.append(i)
    # print(word_positions[type_slice[0] + 1: type_slice[1]])
    type_t = word_positions[type_slice[0] + 1: type_slice[1]]
    coordinates = word_positions[coordinate_slice[0] + 1: coordinate_slice[1]]
    print(f"Found {type_t} at {coordinates}")
    # print(word_positions[coordinate_slice[0] + 1: coordinate_slice[1]])


def new_symbol(old_letter, key_modifier):
    new_letter = chr(ord(old_letter) - key_modifier)
    return new_letter


def decipher_lines(numbers_key):

    new_word = ""
    command = input()

    num_i = 0
    while command != "find":

        for i in range(len(command)):
            new_word += new_symbol(command[i], numbers_key[num_i])
            num_i += 1
            if num_i == len(numbers_key):
                num_i = 0
        display_data(new_word)
        command = input()
        new_word = ""
        num_i = 0


def call_functions():
    numbers_key = [int(x) for x in input().split()]
    decipher_lines(numbers_key)


if __name__ == "__main__":
    call_functions()
