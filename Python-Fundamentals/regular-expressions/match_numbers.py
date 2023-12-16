# Match Numbers
import re


def find_numbers(pattern):
    text = input()
    result = re.findall(pattern, text)
    return result


def call_functions():
    pattern = "((^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s)))"
    match_result = find_numbers(pattern)
    print(" ".join([x[0] for x in match_result]))


if __name__ == "__main__":
    call_functions()
