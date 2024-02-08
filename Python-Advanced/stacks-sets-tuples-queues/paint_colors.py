# Paint Colors
from collections import deque


def call_functions():
    substrings = deque(input().split())

    colors = {
        "all_colors": ["red", "yellow", "blue", "orange", "purple", "green"],
        "found_colors": [],
        "found_secondary_colors": []
    }

    while len(substrings) > 1:
        first_substring = substrings.popleft()
        second_substring = substrings.pop()

        first_concat = first_substring + second_substring
        second_concat = second_substring + first_substring

        if first_concat in colors["all_colors"]:
            colors["found_colors"].append(first_concat)
        elif second_concat in colors["all_colors"]:
            colors["found_colors"].append(second_concat)
        else:
            first_substring = first_substring[:-1]
            second_substring = second_substring[:-1]
            middle_of_substrings = len(substrings) // 2
            if second_substring:
                substrings.insert(middle_of_substrings, second_substring)
            if first_substring:
                substrings.insert(middle_of_substrings, first_substring)
    if len(substrings) == 1:
        last_substring = substrings[0]
        if last_substring in colors["all_colors"]:
            colors["found_colors"].append(last_substring)

    for secondary_color in colors["found_colors"]:
        if secondary_color == "orange":
            if "red" not in colors["found_colors"] or "yellow" not in colors["found_colors"]:
                colors["found_colors"].remove(secondary_color)
        elif secondary_color == "purple":
            if "red" not in colors["found_colors"] or "blue" not in colors["found_colors"]:
                colors["found_colors"].remove(secondary_color)
        elif secondary_color == "green":
            if "yellow" not in colors["found_colors"] or "blue" not in colors["found_colors"]:
                colors["found_colors"].remove(secondary_color)

    print(colors["found_colors"])


if __name__ == "__main__":
    call_functions()
