# Letters Change Numbers


def first_letter_calculation(string_c, lower_alphabet, upper_alphabet, score):
    middle_number = int(string_c[1: -1])
    first_letter = string_c[0]
    if first_letter in upper_alphabet:
        first_index = upper_alphabet.index(first_letter) + 1
        score += middle_number / first_index
    elif first_letter in lower_alphabet:
        first_index = lower_alphabet.index(first_letter) + 1
        score += middle_number * first_index
    return score


def last_letter_calculation(string_c, lower_alphabet, upper_alphabet, score):
    last_letter = string_c[-1]
    if last_letter in upper_alphabet:
        score -= upper_alphabet.index(last_letter) + 1
    elif last_letter in lower_alphabet:
        score += lower_alphabet.index(last_letter) + 1
    return score


def call_functions():
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = lower_alphabet.upper()

    code_string = input().split()
    score = 0
    for string_c in code_string:
        score = first_letter_calculation(string_c, lower_alphabet, upper_alphabet, score)
        score = last_letter_calculation(string_c, lower_alphabet, upper_alphabet, score)
    print(f"{score:.2f}")


if __name__ == "__main__":
    call_functions()
