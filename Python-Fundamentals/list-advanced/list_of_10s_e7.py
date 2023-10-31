# List of 10's
from math import ceil


def range_of_10s(numbers_row):
    numbers = list(map(int, numbers_row.split(", ")))

    lists_tens = [[] for ten in range(1, ceil(max(numbers) / 10) + 1)]

    for ten_step in range(1, ceil(max(numbers) / 10) + 1):
        lists_tens[ten_step - 1] = list(filter(
            lambda x: x if ((ten_step * 10) - 10) < x <= (ten_step * 10) else None, numbers))

    phrase_tens = [f"Group of {tenth * 10}'s: {lists_tens[tenth - 1]}"
                   for tenth in range(1, len(lists_tens) + 1)]
    return phrase_tens


row_of_numbers = input()
for phrase in range_of_10s(row_of_numbers):
    print(phrase)
