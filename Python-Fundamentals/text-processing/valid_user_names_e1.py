# Valid User Names


def valid_usernames(names):
    valid_names = []
    names = names.split(", ")
    for name in names:
        if not 3 <= len(name) < 17 or " " in name:
            continue
        name_check_1 = name.replace("_", "")
        name_check_2 = name_check_1.replace("-", "")
        if name_check_2.isalnum():
            valid_names.append(name)
    return valid_names


if __name__ == "__main__":
    all_names = input()
    for valid in valid_usernames(all_names):
        print(valid)
