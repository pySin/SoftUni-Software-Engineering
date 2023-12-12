# capture the numbers
import re


def find_matches(reg_pattern, reg_text):
    result = re.findall(reg_pattern, reg_text)
    for match in result:
        print(match, end=" ")


pattern = "\d+"
text = input()
while text:
    find_matches(pattern, text)
    text = input()


# for re_match in find_matches(pattern, text):
#     print(re_match, end=" ")
