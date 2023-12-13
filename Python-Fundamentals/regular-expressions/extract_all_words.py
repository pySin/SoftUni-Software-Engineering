# Extract all words
import re

re_pattern = "\w+"
re_text = "_ (Underscores) are also word characters!"


def reg_text(pattern, text):
    words = re.findall(pattern, text)
    return words


for word in reg_text(re_text, re_pattern):
    print(word, end="|")
