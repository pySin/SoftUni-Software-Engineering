# Even Numbers

even_numbers = lambda x: x % 2 == 0


def filter_odd(sequence):
    numbers = list(filter(even_numbers, map(int, sequence.split())))
    return numbers


sequence_numbers = input()
print(filter_odd(sequence_numbers))
