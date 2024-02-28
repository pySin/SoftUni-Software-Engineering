# Numbers dictionary


# def create_dictionary() -> dict:
#     numbers_dictionary = {}
#     command = input()
#
#     while command != "Search":
#         number_text = command
#         try:
#             number_digit = int(input())
#         except ValueError:
#             print("The variable number must be an integer")
#         else:
#             numbers_dictionary[number_text] = number_digit
#
#         command = input()
#     return numbers_dictionary
#
#
# def search_number(numbers_dictionary: dict):
#     command = input()
#     while command != "Remove":
#         try:
#             print(numbers_dictionary[command])
#         except KeyError:
#             print("Number does not exist in dictionary")
#
#         command = input()
#
#
# def remove_number(numbers_dictionary: dict):
#     command = input()
#     while command != "End":
#         number_to_remove = command
#         try:
#             numbers_dictionary.pop(number_to_remove)
#         except KeyError:
#             print("Number does not exist in dictionary")
#         command = input()
#     return numbers_dictionary
#
#
# def call_functions():
#     numbers_dict = create_dictionary()
#     search_number(numbers_dict)
#     numbers_dict = remove_number(numbers_dict)
#     print(numbers_dict)
#
#
# if __name__ == "__main__":
#     call_functions()


# -- Atanas Atanasov's solution

numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    try:
        number = int(input())
    except ValueError:
        print("The variable number must be an integer")
    else:
        numbers_dictionary[number_as_string] = number
    line = input()

line = input()
while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

line = input()
while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

print(numbers_dictionary)
