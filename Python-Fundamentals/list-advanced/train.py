# Train

# print("Test it!")

# my_list = [num for num in range(1, 11) if num % 2 == 0]
# print(my_list)

# num_sequence = (2, 3, 4, 5)
# sequence_on_power = [x**2 for x in num_sequence]
# print(sequence_on_power)

# letters = ["a", "b", "c", "d", "e"]
# uppercase_letters = [letter.upper() for letter in letters]
# print(uppercase_letters)

# words = ["hello", "python", "and", "other", "snakes"]
# filtered_words = [word.upper() for word in words if "t" in word]
# print(filtered_words)

# IF statements in comprehension

# numbers = [1, 2, 3, 4, 5]
# modified_nums = [num * 2 if num < 3 else num * 4 for num in numbers]
# print(modified_nums)


# -- Extend

# fruits = ["apple", "banana"]
# more_fruits = ["elderberry", "blueberry"]
# fruits.extend(more_fruits)
# fruits = fruits + more_fruits
# print(fruits)

# -- Insert

# fruits = ["apple", "cherry"]
# fruits.insert(1, "strawberry")
# print(fruits)

# -- Clear

# fruits = ["apple", "cherry"]
# fruits.clear()
# print(fruits)


# -- pop()

# fruits = ["apple", "cherry"]
# last_fruit = fruits.pop()
# print(fruits)
# print(f"Last fruit: {last_fruit}")

# -- remove()

# fruits = ["apple", "cherry", "pear", "cherry"]

# filtered_cherry = [fruit for fruit in fruits if fruit != "cherry"]

# for i in range(len(fruits) - 1, -1, -1):
#     print(i)
#     if fruits[i] == "cherry":
#         fruits.pop(i)
#
# print(fruits)
# print(filtered_cherry)


# def pals(word):
#     return word == word[::-1]
#
#
# words = ["wow", "non", "happy", "Better"]
# pal_words = [word for word in words if pals(word)]
# print(pal_words)

# -- map() function

# numbers = [1, 2, 3, 4, 5]
#
# pow_numbers = map(lambda x: x ** 2, numbers)
# print(list(pow_numbers))
#
# names = ["Ema", "Toto", "Azis"]
#
# capital_names = [name.capitalize() for name in names]
# reversed_capital = map(lambda x: x[::-1], capital_names)
# print(capital_names)
# print(list(reversed_capital))

# -- Filter

# numbers = [1, 2, 3, 4, 5]
#
# filtered_numbers = filter(lambda x: x > 3, numbers)
# print(list(filtered_numbers))

# -- Swap Numbers

# numbers = [1, 2, 3, 4, 5]
#
# numbers[0], numbers[1] = numbers[1], numbers[0]
# print(numbers)

# -- Set

# numbers = [1, 2, 3, 4, 5, 1, 4, 6, 2]
# unique_numbers = list(set(numbers))
# print(unique_numbers)
#
# # works with strings as well
#
# word = "hello"
# unique_chars = list(set(word))
# print(unique_chars)


# -----
# from math import ceil
# change_list = [2, 57, 3, 74, 92, 11]
#
#
# def increase_even(even_list):
#     increased_even_list = [number * 2 for number in even_list]
#     return increased_even_list
#
#
# def increase_odd(odd_list):
#     increased_odd_list = [ceil(number * 1.55) for number in odd_list]
#     return increased_odd_list
#
#
# def change_numbers(initial_numbers):
#     even_numbers = [number for number in initial_numbers if number % 2 == 0]
#     odd_numbers = [number for number in initial_numbers if number % 2 != 0]
#     increased_even_numbers = increase_even(even_numbers)
#     increased_odd_numbers = increase_odd(odd_numbers)
#     return increased_even_numbers, increased_odd_numbers
#
#
# separated_even_numbers, separated_odd_numbers = change_numbers(change_list)
# print(separated_even_numbers)
# print(separated_odd_numbers)

# map() with lambda


# current_sequence = [1, 5, 88, 26, 57, 265, 99]
#
# through_function_sequence = list(map(lambda x: x if x > 50 else 0, current_sequence))
# print(current_sequence)
# print(through_function_sequence)

# -------
# sorted() with lambda

# current_sequence = [1, 5, 88, 26, 57, 265, 99, 120]
#
# sorted_sequence = sorted(current_sequence, key=lambda x: x % 2)
# print(sorted_sequence)
#
# sorted_sequence_2 = sorted(current_sequence, key=lambda x: 100 - x if x < 100 else x - 100)
# print(sorted_sequence_2)

# ----

# filter() with lambda


# current_sequence = [1, 5, 88, 26, 57, 265, 99]
# filtered_sequence = list(filter(lambda x: 20 < x < 90, current_sequence))
# print(filtered_sequence)


# ------

# sort() with lambda


# current_sequence = [1, 5, 88, 26, 57, 265, 99]
# s_sequence = current_sequence.sort(key=lambda x: x - 100 if x > 100 else 100 - x)
# print(current_sequence)

# list_2 = [1, 2, 3, 4, 5, 6]
#
# list_2 = list(filter(lambda x: x if x > 2 else x > 2, list_2))
# print(list_2)

# word_split = "word".split()
# print(word_split)

# print(5 // 5)

