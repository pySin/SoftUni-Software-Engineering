# Find Variable Names in sentences

import re


def find_matches(reg_pattern, reg_text):
    result = re.finditer(reg_pattern, reg_text)
    result_list = []
    for match in result:
        # print(match)
        result_list.append(match.group(2))
    print(",".join(result_list))


pattern = "(\s_)([a-zA-Z]+\\b)"
text = input()

find_matches(pattern, text)

