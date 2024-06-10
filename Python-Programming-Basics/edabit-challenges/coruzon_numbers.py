# Curzon numbers


def is_curzon(num):
    if ((2 ** num) + 1) % ((2 * num) + 1) == 0:
        return True
    else:
        return False


current_number = int(input())
print(is_curzon(current_number))
