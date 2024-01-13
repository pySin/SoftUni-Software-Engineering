
# -- pop elements from 1 list and put them into another
# first_collection = [1, 2, 3, 4, 5]
# second_collection = [first_collection.pop() for i in range(len(first_collection))
#                      if first_collection[i - 1] > 3]
# print(f"Second collection: {second_collection}")

# -- Unpack and separate

# first_collection = [1, 2, 3, 4, 5]
# print(*first_collection, sep="|")

# -- Delete a slice

# first_collection = [1, 2, 3, 4, 5, 6, 7, 8]
# del first_collection[2:4]
# print(first_collection)


# a = [1, 2, 3, 4, 5]
# del a[3]
# print(a)

# print(bool(None))
# print(bool(-1))
# print(bool(0))
# print(bool(""))

# -- One lite if else

# balance = 15
# interest = 1.1 if balance < 5 or balance == 13 or balance == 14 else 0.9
# print(interest)

# -- usage of "*"

# values = [1, 2, 3, 4]
# print("Numbers are: " + str(map(str, *values)))
#
# unpacked = {
#     "sum_it": lambda a, b, c, d: a + b + c + d
#     }
#
# print(unpacked["sum_it"](*values))

# --
# icecreams = {'vanilla': 3, 'chocolate': 2, 'strawberry': 2}
#
# key_1, key_2, key_3 = icecreams
# print(key_2)

# --

# first, *unused, before, last = [1, 2, 3, 5, 7]
#
# print(before)
# print(unused)

# -- packing

# *unused, before, last = [1, 7]  # * can grab None as well
#
# print(before)
# print(unused)


# --
# m1, *m2 = 1, 3, 5, 7
# print(m2)

# --
*string, = 'PythonIsTheBest'
print(string)
print(type(string))

