import os


sub_dir = "inner_dir"
dir_path = os.getcwd()
file_name = "text_1.txt"
full_path = os.path.join(dir_path, sub_dir, file_name)

with open(full_path) as f:
    print(f.read())
