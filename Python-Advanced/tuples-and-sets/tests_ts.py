# tests


# print("Test working!")
# tuple_num = (6,)
# print(tuple_num)
# print(type(tuple_num))


# def add_hundred(data):
#     data.append(28)
#
#
# list_data = [1, 2, 3]
# tuple_data = tuple(list_data)
# list_data_2 = list_data
#
# add_hundred(list_data)
# print(list_data)
# print(tuple_data)
# print(list_data_2)


# collection_a = ([1, 2, 3], 7)
# collection_a[0][0] = 55
# print(collection_a)

# one_list = [1, 2, 3]
# two_list = one_list.copy()
# one_list[0] = 55
# print(one_list)
# print(two_list)
# print(id(one_list))
# print(id(two_list))


# --- Tuple Unpacking

# lizz = [1, 2, 3]
# a, b, c = lizz
# print(b)

# Sets can work with some operators: | - union,

# a = {1, 2, 3, 1, 4}
# my_set = {1, 2, 3, 1, 1.3, 1.2}

# result = a | my_set  # Union with sets
# print(result)

# result_2 = a & my_set  # Intersection with sets
# print(result_2)
#
# result_3 = a < my_set
# print(result_3)
# print({1, 2} < {1, 2, 3})
#

# -- difference
# diff = my_set - a
# diff_2 = a - my_set
# print(diff)
# print(diff_2)
#
# sym_diff = a ^ my_set
# print(sym_diff)

# -- Set Comprehensions

# nums = [1, 2, 3, 4, 4, 5, 6, 2, 1]
# unique = {num for num in nums}
# print(unique)

# print({1, 2, 3} - {1, 2})


# -- Sorted puts the set elements in a list

# unsorted_set = {1, 2, 5, 3, 6, 4}
# sorted_set = sorted(unsorted_set)
# print(id(unsorted_set))
# print(id(sorted_set))
# print(unsorted_set)
# print(sorted_set)


# unsorted = [1, 3, 2, False, True]
# unsorted.sort()
# print(unsorted)

# def summation(a, b):
#     return a + b
#
#
# two_numbers = [1, 2]
#
# summed = summation(*two_numbers)
# print(summed)
#
# first_number, second_number = two_numbers
# print(first_number)

# -- Update set with list


# uni_col = {1, 2, 3}
# non_uni_list = [4, 4, 5, 6, 4, 7, 6, 6]
#
# uni_col.update(non_uni_list)
# print(uni_col)

# set_1 = {1, 2, 3, 5}
# set_2 = {4, 3, 6, 7}
#
# combined_set = set_2.union(set_1)
# print(combined_set)

# --

# numb = 3
# print(f"{numb:02d}")

# set_1 = {1, 2, 3, 5}
# set_2 = {4, 3, 6, 7, 8, 9, 1}
#
# print(set_1 - set_2)

# -- Advanced Print


# chocolates = ["white", "dark", "milky"]
# chocolates = []

# print(f"Chocolates: {', '.join([choc for choc in chocolates]) if len(chocolates) >= 3 else [chocolates.index(choc) for choc in chocolates]}")

# bread = 1
# materials = [1, 2, 3, 4, 5]
# magic = []
#
# material = materials.pop() if magic or not bread or (2 + 2) == 5 else 0
# print(material)

# from collections import deque
#
# materials = deque([1, 2, 3, 4, 5])
# print(materials[-3])
# print(materials[-3])

# print(1 // 2)

# -- Single Line element pop with if

# my_list = [1]
# first_pop = my_list.pop()
# second_pop = my_list.pop() if my_list else None
# print(first_pop)
# print(second_pop)

# --

# main_nums = [1, 2, 3]
# second_nums = {
#     "one": ["three", "four"],
#     "five": ["six", "seven"]
# }
#
# new_nums = []
# new_nums.append(second_nums["one"])
# print(new_nums)

# single element tuple

# tup_1 = (1, )
#
# print(type(tup_1))

# Set recall

# collection = [1, 2, 3, 5, 12, 44, 1, 2]
# print(set(collection))

# -- Sets Operations

# u_collection = {1, 2, 3, 5, 12, 44, 77}
# u_collection_2 = {1, 2, 3, 5, 12, 44, 33, 22}
# u_collection_3 = {1, 2, 3}

# u_collection_result = u_collection | u_collection_2  # union operator(all unique)
# u_collection_result = u_collection & u_collection_2  # intersection operator(found in both sets)
# u_collection_result = u_collection > u_collection_3  # subset operator(set > subset)
# u_collection_result = u_collection - u_collection_3  # diff operator(whit in A is not present in B)
# u_collection_result = u_collection ^ u_collection_2  # symmetric difference(non-matching elements from both sets)

# print(u_collection_result)

# --

