# Odd and Even Sums


def odd_even_sums(base_num_string):
    even_sum = 0
    odd_sum = 0
    for num_string in base_num_string:
        str_to_int = int(num_string)
        if str_to_int % 2 == 0:
            even_sum += str_to_int
        else:
            odd_sum += str_to_int
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


base_number = input()
print(odd_even_sums(base_number))
