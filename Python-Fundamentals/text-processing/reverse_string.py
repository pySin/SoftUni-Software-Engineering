# Reverse String


def reverse(single_string):

    reversed_string = single_string[::-1]
    return reversed_string


def print_reversed():
    command = input()
    while command != "end":
        reversed_result = reverse(command)
        print(f"{command} = {reversed_result}")

        command = input()


if __name__ == "__main__":
    print_reversed()
