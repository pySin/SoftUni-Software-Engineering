# Letters Change Numbers

def extract_number(sequence):
    number = int(sequence[1:-1])
    return number


def sequence_result(sequence):

    current_result = 0

    lower_alphabet = "abcdefghijklmnopqrstuvwyz"
    upper_alphabet = lower_alphabet.upper()  # [1:]
    if sequence[0] in lower_alphabet:
        current_result += (extract_number(sequence) * (lower_alphabet.index(sequence[0]) + 1))
    else:  # If the letter is uppercase
        current_result = (extract_number(sequence) / (upper_alphabet.index(sequence[0]) + 1))

    if sequence[-1] in lower_alphabet:
        current_result += lower_alphabet.index(sequence[-1]) + 1
    else:
        current_result -= upper_alphabet.index(sequence[-1]) + 1

    return current_result


if __name__ == "__main__":
    row = input().split()
    final_result = 0
    for piece in row:
        final_result += sequence_result(piece)
    print(f"{final_result:.2f}")
