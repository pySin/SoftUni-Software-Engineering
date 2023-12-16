# Match Full Name
import re

# re_pattern = "^[A-Z][a-z]+\s[A-Z][a-z]+,|\s[A-Z][a-z]+\s[A-Z][a-z]+,|\s[A-Z][a-z]+\s[A-Z][a-z]+$"
re_pattern = "\\b[A-Z][a-z]+\s[A-Z][a-z]+\\b"
re_text = input()


def reg_text(pattern, text):
    words = re.findall(pattern, text)
    return words


for name in reg_text(re_pattern, re_text):
    print(name, end=" ")

