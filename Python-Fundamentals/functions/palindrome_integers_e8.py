# Palindrome Integers

def palindrome(numbers_as_str):
    int_strings = numbers_as_str.split(", ")
    [print(number_str == number_str[::-1]) for number_str in int_strings]


palindrome(input())
