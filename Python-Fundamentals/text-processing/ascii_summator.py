# ASCII Sumator


def get_ascii_range():
    char_1 = ord(input())
    char_2 = ord(input())
    return char_1, char_2


def inbound_sum(lower_bound, upper_bound, string):
    sum_result = 0
    for i in range(len(string)):
        if lower_bound < ord(string[i]) < upper_bound:
            sum_result += ord(string[i])
    return sum_result


def call_functions():
    lower_bound, upper_bound = get_ascii_range()
    sum_result = inbound_sum(lower_bound, upper_bound, input())
    print(sum_result)


if __name__ == "__main__":
    call_functions()
