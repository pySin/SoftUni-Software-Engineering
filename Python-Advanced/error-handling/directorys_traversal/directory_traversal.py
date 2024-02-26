# Directory Traversal
# import os
#
#
# def file_names() -> list:
#     files = os.listdir()
#     return files
#
#
# def files_dictionary(files_list: list) -> dict:
#     files_dict = {}
#     for file in files_list:
#         if os.path.isfile(file):
#             name, extension = file.split(".")
#             if extension in files_dict:
#                 files_dict[extension].append(file)
#             else:
#                 files_dict[extension] = [file]
#         else:
#             print(file)
#     return files_dict
#
#
# def data_to_file(files_dict: dict):
#     with open("report.txt", "a") as f:
#         for extension, files_list in sorted(files_dict.items()):
#             f.write(f".{extension}\n")
#             for file in sorted(files_list):
#                 f.write(f"- - - {file}\n")
#
#
# def call_functions():
#     files_list = file_names()
#     files_dict = files_dictionary(files_list)
#     data_to_file(files_dict)
#
#
# if __name__ == "__main__":
#     call_functions()


# Atanas Atanasov's solution

import os
directory = "../"
files = {}
def get_files(folder, level):
    if level < 0:
        return
    for element in os.listdir(folder):
        f = os.path.join(folder, element)
        if os.path.isfile(f):
            extension = element.split(".")[-1]
            if extension not in files:
                files[extension] = []
            files[extension].append(element)
        else:
            get_files(f, level - 1)


get_files(directory, 2)
with open(os.path.join(directory, "report.txt"), "w") as output_file:
    for ext, f_names in sorted(files.items()):
        output_file.write(f".{ext}\n")
        for f_name in sorted(f_names):
            output_file.write(f"- - - {f_name}\n")
