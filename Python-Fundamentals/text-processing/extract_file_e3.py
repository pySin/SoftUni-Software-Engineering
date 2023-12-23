# Extract File


def get_filename_in_path(file_path):
    file_name = file_path.split("\\")[-1]
    return file_name


def name_and_extension(file_path):
    file_name = get_filename_in_path(file_path)
    name_extension = file_name.split(".")
    return name_extension


if __name__ == "__main__":
    path = input()
    name_file_type = name_and_extension(path)
    print(f"File name: {name_file_type[0]}")
    print(f"File extension: {name_file_type[1]}")
