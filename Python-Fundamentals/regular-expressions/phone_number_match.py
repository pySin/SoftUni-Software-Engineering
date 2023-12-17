# Phone Number Match

import re

# re_pattern = "\\b\+359[\s-]2[\s-]\d{3}[\s-]\d{4}\\b"
re_pattern = "\+359[\s]2[\s]\d{3}[-\s]\d{4}\\b|\+359[-]2[-]\d{3}[-\s]\d{4}\\b"
re_text = input()


def reg_text(pattern, text):
    words = re.findall(pattern, text)
    return words


print(', '.join(reg_text(re_pattern, re_text)))
