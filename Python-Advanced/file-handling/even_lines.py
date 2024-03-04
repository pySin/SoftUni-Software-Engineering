# # Even Lines
#
#
# def file_to_list() -> list:
#     with open("text.txt", "r") as f:
#         file_list = f.readlines()
#     return file_list
#
#
# def change_symbols(file_list: list) -> list:
#     chars = ["-", ",", ".", "!", "?"]
#     new_lines = []
#     for line in file_list:
#         for char in chars:
#             line = line.replace(char, "@")
#         new_lines.append(line)
#     return new_lines
#
#
# def revert_word_order(new_lines: list):
#
#     for i in range(len(new_lines)):
#         new_lines[i] = new_lines[i].split()[::-1]
#     return new_lines
#
#
# def display_lines(new_lines: list):
#     [print(" ".join(new_lines[i])) for i in range(len(new_lines)) if i % 2 == 0]
#
#
# def call_functions():
#     file_list = file_to_list()
#     file_list = change_symbols(file_list)
#     new_lines = change_symbols(file_list)
#     new_lines = revert_word_order(new_lines)
#     display_lines(new_lines)
#
#
# if __name__ == "__main__":
#     call_functions()

# -- Atanas Atanasov's solution

with open("text.txt") as f:
    for row, line in enumerate(f.readlines()):
        if row % 2 == 0:
            for ch in "-,.!?":
                line = line.replace(ch, "@")
            print(" ".join(reversed(line.split())))


