# # Anonymous Threat
#
#
# def words_change(base_words):
#
#     command = input()
#
#     while command != "3:1":
#
#         instructions = command.split()
#
#         if instructions[0] == "merge":
#             first_index = int(instructions[1])
#             second_index = int(instructions[2])
#
#             if first_index < 0:
#                 first_index = len(base_words) + first_index
#
#             if second_index < 0:
#                 second_index = len(base_words) + second_index
#
#             merged_indexes = ""
#
#             if first_index < 0:
#                 if 0 < second_index < len(base_words):
#                     merged_indexes = "".join(base_words[:second_index + 1])
#             elif 0 <= first_index < len(base_words):
#                 if second_index >= len(base_words):
#                     merged_indexes = "".join(base_words[first_index:])
#                 elif 0 <= first_index < len(base_words) and 0 < second_index < len(base_words):
#                     if first_index < second_index:
#                         merged_indexes = "".join(base_words[first_index:second_index + 1])
#                         # print(merged_indexes)
#
#             if merged_indexes:
#                 if first_index < 0:
#                     base_words = base_words[second_index + 1:]
#                     base_words.insert(0, merged_indexes)
#                 elif second_index >= len(base_words):
#                     base_words = base_words[:first_index]
#                     base_words.append(merged_indexes)
#                 elif first_index < second_index:
#                     base_words = base_words[:first_index] + base_words[second_index + 1:]
#                     base_words.insert(first_index, merged_indexes)
#
#         if instructions[0] == "divide":
#             # print("In Divide")
#             target_index = int(instructions[1])
#             divider = int(instructions[2])
#             sub_length = len(base_words[target_index]) // divider
#             divided = []
#             for i in range(0, len(base_words[target_index]), sub_length):
#                 piece = base_words[target_index][i:i+sub_length]
#                 divided.append(piece)
#             # print(divided)
#             base_words.pop(target_index)
#             for j in range(len(divided) - 1, - 1, -1):
#                 base_words.insert(target_index, divided[j])
#             # base_words.insert(target_index, divided)
#
#         command = input()
#
#     return base_words
#
#
# def call_functions():
#     base_words = input().split()
#     base_words = words_change(base_words)
#     print(" ".join(base_words))
#
#
# if __name__ == "__main__":
#     call_functions()

# Anonymous Threat


def words_change(base_words):

    command = input()

    while command != "3:1":

        instructions = command.split()

        if instructions[0] == "merge":
            first_index = int(instructions[1])
            second_index = int(instructions[2])
            if first_index < 0 and second_index >= len(base_words):
                items_range = base_words[0: len(base_words)]
                combined_words = "".join(items_range)
                base_words = []
                base_words.insert(first_index, combined_words)
            elif second_index > len(base_words):
                items_range = base_words[first_index:]
            elif first_index < 0:
                items_range = base_words[:second_index + 1]
                first_index = 0
            else:
                items_range = base_words[first_index:second_index + 1]

            if len(items_range) < 1:
                command = input()
                continue

            combined_words = "".join(items_range)
            base_words = base_words[:first_index] + base_words[second_index + 1:]
            base_words.insert(first_index, combined_words)

        if instructions[0] == "divide":
            # print("In Divide")
            target_index = int(instructions[1])
            divider = int(instructions[2])
            sub_length = len(base_words[target_index]) // divider
            remainder = len(base_words[target_index]) % divider
            divided = []
            for i in range(0, divider * sub_length, sub_length):
                piece = base_words[target_index][i: i + sub_length]
                # piece = base_words[target_index][i:i+sub_length]
                divided.append(piece)
            # print(divided)
            if remainder > 0:
                divided[-1] = divided[-1] + base_words[target_index][-remainder:]

            base_words.pop(target_index)

            for j in range(len(divided) - 1, - 1, -1):
                base_words.insert(target_index, divided[j])

            # base_words.insert(target_index, divided)

        command = input()

    return base_words


def call_functions():
    base_words = input().split()
    base_words = words_change(base_words)
    # print(base_words)
    print(" ".join(base_words))


if __name__ == "__main__":
    call_functions()
