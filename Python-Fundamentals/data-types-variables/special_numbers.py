# Special Numbers


n = int(input()) + 1

for i in range(1, n):
    num_to_str = str(i)
    split_single_numbers = list(map(int, list(num_to_str)))
    if sum(split_single_numbers) in [5, 7, 11]:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")

