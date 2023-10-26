# Lecture Lists


# list_example = [1, 1.5, {"name": "Blagoi"}, True, False, ["hi", "there"]]
#
# print(list_example)
# print(type(list_example))
# print(list(range(1, 6)))

# my_text = "a, b, c, d, e"
# split_text = my_text.split(", ")
# print(split_text)

# data = input().split(", ")
# print(data)

# max_list_split = "a, b, c, d"
# split_string = max_list_split.split(", ", 2)
# print(split_string)

# my_list = ["a", "b", "c"]
# joined_list = "^-^".join(my_list)
# print(joined_list)

# num_lists = [1, 2, 3, 4, 5, 6]
# print("--".join([str(i) for i in num_lists]))
# print(num_lists[-1])

# my_list = [1, 2, 3, 3]
# my_list.remove(3)
# print(my_list)

fruits = ["apple", "banana", "guava"]
index_fruit = 0

# while index_fruit < len(fruits):
#     print(fruits[index_fruit])
#
#     index_fruit += 1

# words = ["human", "lion", "rabbit", "giraffe"]
#
# word_index = 0
#
# while word_index < len(words):
#     current_word = words[word_index]
#     modified_word = ''
#
#     for char in reversed(current_word):
#         modified_word += char.upper()
#
#     print(modified_word)
#     word_index += 1


# list_in = ["camel", "mummy", "pyramid", "pharao"]
#
# if "pharao" in list_in:
#     print(f"\"pharao\" is in list_in!")
# else:
#     print("Cherry not found!")

elements = [1, 2, 3, 4, 5]

search_element = 4
print("Number " + str(search_element) + " in index: " + str(elements.index(search_element)))
