# Equal Pairs

number_of_pairs = int(input())
initial_pairs = 0
top_difference = 0

last_pair = 0
last_difference = 0

x = 0
y = "yes"
for _ in range(number_of_pairs):
    first_pair_number = int(input())
    second_pair_number = int(input())

    if initial_pairs == 0 and x == 0:
        initial_pairs = first_pair_number + second_pair_number
        x += 1

    elif initial_pairs != first_pair_number + second_pair_number:
        y = "no"

    if _ != 0:
        last_difference = abs((first_pair_number + second_pair_number) - last_pair)
        if last_difference > top_difference:
            top_difference = last_difference

    last_pair = first_pair_number + second_pair_number

if y == "yes":
    print(f"Yes, value={initial_pairs}")
else:
    print(f"No, maxdiff={top_difference}")
