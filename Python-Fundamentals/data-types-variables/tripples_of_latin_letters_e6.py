# Triples of latin letters

alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_range = int(input())

for first_letter in range(letter_range):
    for second_letter in range(letter_range):
        for third_letter in range(letter_range):
            print(alphabet[first_letter] + alphabet[second_letter] + alphabet[third_letter], end="")
            print()
