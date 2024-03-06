# Test

# print("Test")


# number = int(input())
#
# print(number)


# --

# email = input()
#
# file = open("user.txt", "r")
# file.write("Something")
#
# # file.close()
# print(email)
# print(file.name)

# --

# file = open("./m_dir/ines.txt", "r")
# file = open("C:\\Users\\Lenovo\\PycharmProjects\\SoftUniFundamentals"
#             "\\PythonAdvanced\\file_handling\m_dir\\ines.txt", "w")
# # file = open("C:Users/Lenovo/PycharmProjects/SoftUniFundamentals/m_dir/ines.txt", "r")
# file.write("Something 11")
#
# print(file)


# Get path to current directory

# import os


# WORKING_DIRECTORY_PATH = os.getcwd()
# file_path = WORKING_DIRECTORY_PATH + "/m_dir/ines.txt"

# file_path = os.path.join(WORKING_DIRECTORY_PATH, "m_dir", "ines.txt")


# file = open(file_path, "w")
# file.write("The only one!")

# --
# import os
#
# WORKING_DIRECTORY_PATH = os.getcwd()
# file_path = os.path.join(WORKING_DIRECTORY_PATH, "some.txt")
#
# file = open(file_path, "r")
# print(file.read(2))
# print(file.read(2))  # Moving the cursor

# --
# import os
#
# WORKING_DIRECTORY_PATH = os.getcwd()
# file_path = os.path.join(WORKING_DIRECTORY_PATH, "some.txt")
#
# file = open(file_path, "r")
# for _ in range(100):
#     print(file.read(2))

# --
# import os
#
# WORKING_DIRECTORY_PATH = os.getcwd()
# file_path = os.path.join(WORKING_DIRECTORY_PATH, "some.txt")
#
# file = open(file_path, "r")
# print(file.readline())
# print(file.readline())
# print(file.readlines())

# for line in file.readlines():
#     print(line)
# print(file.readlines(5))
# [print(line, end="") for line in file.readlines()]

# for line in file:  # saves memory / read + simple loop
#     print(line)

# --

# import os
#
# WORKING_DIRECTORY_PATH = os.getcwd()
# file_path = os.path.join(WORKING_DIRECTORY_PATH, "some.txt")
#
# file = open(file_path, "a")
# file.write("???")


# -- writelines()

# import os
#
# WORKING_DIRECTORY_PATH = os.getcwd()
# file_path = os.path.join(WORKING_DIRECTORY_PATH, "some.txt")
#
# file = open(file_path, "a")
# list_data = ["2", "1", "5", "67", "hi"]
# file.writelines([f"{item}\n" for item in list_data])

# -- USE with construct


# import os
#
# WORKING_DIRECTORY_PATH = os.getcwd()
# file_path = os.path.join(WORKING_DIRECTORY_PATH, "some.txt")

# file = open(file_path, "a")
# print(file.closed)
# file.write("Hello")
# file.close()
# print(file.closed)

# >> -- OR the proper

# with open(file_path, "a") as f:
#     f.write("Hello\n")
#
# print(f.closed)

# --

# import os
#
# WORKING_DIRECTORY_PATH = os.getcwd()
# file_path = os.path.join(WORKING_DIRECTORY_PATH, "some.txt")
#
#
# with open(file_path, "r") as f:
#     string_1 = f.read()
#
# print(string_1)


# -- check correct file path

# file_path = input("Provide correct file path")
#
# try:
#     with open(file_path, "r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("File was not found")

# ->- Delete files

# import os
#
# FOLDER_PATH = os.getcwd()
# FILE_NAME = "text.txt"
# FULL_PATH = os.path.join(FOLDER_PATH, FILE_NAME)
# # with open(FULL_PATH, "w") as f:
# #     f.write("Hello ohlio")
# print(FULL_PATH)
#
# if os.path.exists(FULL_PATH):
#     os.remove(os.path.join(FULL_PATH))
#     print("File Removed")
# else:
#     print("File don't exist")

# os.remove("text.txt")

# -- A bit of matrix recall


# with open("text.txt", "w") as f:
#     pass


# - use redlines

# with open("text.txt", "r") as f:
#     lines_list = f.readlines()
# print(lines_list)

# -- Use enumerate start=5

# list_1 = ["a", "b", "c"]
# enumerated = enumerate(list_1, start=5)
# print(list(enumerated))

# --

# text = "First line\nSecond line\n"
# text.replace("First", "1st")
# print(text)

# -- Open two files at the same time

# with open("text.txt") as o_file, open("output.txt", "w") as output_file:

# -- Get the rest of values in *args

# arguments = ["Add", "FileMaya", 3, 4, 5]
# command, file_name, *args = arguments  # remaining values
# print(command)
# print(file_name)
# print(args)

# -- Create a file and close it

# open("text.txt", "w").close()

# -- Check if file exists

# if os.path.exists(filename):

# -- directory level

# import os
# directory = "./"
# for base, dirs, filenames in os.walk(directory):
#     # print(base)
#     print(dirs)
#     # print(filenames)

# -- Minus operation

# num = 3
# sub = -1
# print(num + sub)
# print(num - sub)

# -- Return Boolean in List Comprehension

# numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# search_num = [[num == 1 for num in row] for row in numbers]  # The result is an evaluation.
# print(search_num)

# -- if None return False

# var_1 = None
# if var_1:
#     print("None is true")
# else:
#     print("None is False as well")

# -- all() for rows

# rows = [[1, 2, 3], [1, 2, 3], [1, 3, 2]]
# is_1_2 = all([2 in row for row in rows])
# print(is_1_2)

# -- None is uniquely counted

# list_with_none = ["X", "O", None]
# print(len(set(list_with_none)))

# -- Double dictionary comprehension

# number = 4
# nums_dict = {i: [i // number, i % number] for i in range(number ** 2)}
# for item in nums_dict.items():
#     print(item)

# --

# all(), any()

# nums = [3, 6, -4, -67, 55]
# pos = [1, 3, 66, 89]
# neg = [-12, -6, -78]
#
#
# def positives(num):
#     return True if num >= 0 else False
#
#
# def negatives(num):
#     return True if num < 0 else False
#
#
# print(all([positives(x) for x in nums]))
# print(all([positives(x) for x in pos]))
# print(any([negatives(x) for x in nums]))
# print(all([negatives(x) for x in neg]))
#
# evaluations = [num < 0 for num in nums]
# print(evaluations)



