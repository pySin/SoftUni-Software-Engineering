# Find dates


import re

re_pattern = "(\d{2})([-./])([A-Z][a-z]{2})\\2(\d{4})"
re_text = input()


def reg_text(pattern, text):
    words = re.finditer(pattern, text)
    return words


for date_match in reg_text(re_pattern, re_text):
    day = date_match.group(1)
    separator = date_match.group(0)
    month = date_match.group(3)
    year = date_match.group(4)
    print(f"Day: {day}, Month: {month}, Year: {year}")

# for date in reg_text(re_pattern, re_text):
#     print(f"Day: {date[0]}, Month: {date[2]}, Year: {date[3]}")


# for date in reg_text(re_pattern, re_text):
#     print(f"Day: {date[0:2]}, Month: {date[3:6]}, Year: {date[7:]}")
