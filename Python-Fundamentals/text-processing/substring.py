# Substring

def remove_substrings(original_string, substring):
    while substring in original_string:
        original_string = original_string.replace(substring, "", 1)
    return original_string


if __name__ == "__main__":
    main_string = input()
    sub_string = input()
    print(remove_substrings(sub_string, main_string))
