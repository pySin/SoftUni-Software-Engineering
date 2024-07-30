# Functions To Test


def get_even_numbers(number_list):
    even_number_list = []

    for i in range(len(number_list)):
        if number_list[i] % 2 == 0:
            even_number_list.append(number_list[i])

    return even_number_list


# even_numbers = get_even_numbers([2, 3, 6, 7, 8])
# print(even_numbers)
