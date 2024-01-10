# Numbers

numbers_row = input()


def five_biggest(row_of_numbers):
    numbers_available = list(map(int, row_of_numbers.split()))
    # print(numbers_available)
    average_number = sum(numbers_available) / len(numbers_available)
    # print(average_number)
    bigger_than_average = [number for number in numbers_available if number > average_number]
    if not bigger_than_average:
        return "No"
    bigger_than_average.sort(reverse=True)
    if len(bigger_than_average) > 5:
        bigger_than_average = bigger_than_average[:5]
    return bigger_than_average


results = five_biggest(numbers_row)
print(*results)
