# Extract the links
import re


def extract_link(pattern, text):
    result = re.findall(pattern, text)
    if result:
        link = result[0][0]
        return link


def call_functions():
    reg_pattern = "(www\.[a-zA-Z0-9-]+(\.[a-z-]+)+)"
    text = input()
    while text:
        link = extract_link(reg_pattern, text)
        if link:
            print(link)
        text = input()


if __name__ == "__main__":
    call_functions()
