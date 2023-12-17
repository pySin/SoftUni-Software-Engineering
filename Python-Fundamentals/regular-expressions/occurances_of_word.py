# Occurrences of word
import re

text = input()
condition = input()
pattern = f"\\b{condition}\\b"


def occurrences(reg_pattern, reg_text):
    result = re.findall(reg_pattern, reg_text, re.IGNORECASE)
    return result


print(len(occurrences(pattern, text)))
#print(occurrences(pattern, text))
