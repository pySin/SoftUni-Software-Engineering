# Messaging


number_sequence = input().split()
letter_sequence = list(input())

phrase = ""

for i in range(len(number_sequence)):
    current_number = sum([int(number) for number in number_sequence[i]])
    if current_number >= len(letter_sequence):
        current_number -= len(letter_sequence)
        phrase += letter_sequence[current_number]
        letter_sequence.pop(current_number)
    else:
        phrase += letter_sequence[current_number]
        letter_sequence.pop(current_number)

print(phrase)
