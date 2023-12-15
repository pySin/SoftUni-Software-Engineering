# Furniture
import re


def furniture(reg_pattern, reg_text):

    result = re.findall(reg_pattern, reg_text)
    # print(result)
    return result


def calculate_total():
    text = input()
    pattern = "^>>(\w+)<<(\d+\.{0,1}\d*)!(\d+)"
    total = 0

    print("Bought furniture:")
    while text != "Purchase":
        result_find = furniture(pattern, text)
        # print(result_find)
        if result_find:
            print(result_find[0][0])
            total += (float((result_find[0][1])) * float((result_find[0][2])))

        text = input()

    print(f"Total money spend: {total:.2f}")


calculate_total()
