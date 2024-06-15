# -- any([]) function

nums = [1, 3, 9]
nums_2 = [1, 3, 4]
nums_3 = [11, 6, 9]


def check_nums(numbers: list):
    evaluations = [True if n < 5 else False for n in numbers]
    return evaluations


for seq in (nums, nums_2, nums_3):
    print(f"Is any True: {any(check_nums(seq))}")
    print(f"Are all True: {all(check_nums(seq))}")