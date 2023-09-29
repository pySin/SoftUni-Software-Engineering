# Gold Mine

mines_count = int(input())

for i in range(mines_count):
    expected_gold_yield = float(input())

    days_to_dig = int(input())
    all_real_gold_yield = 0
    for j in range(days_to_dig):
        gold_per_day = float(input())
        all_real_gold_yield += gold_per_day

    real_gold_yield = all_real_gold_yield / days_to_dig
    if real_gold_yield >= expected_gold_yield:
        print(f"Good job! Average gold per day: {real_gold_yield :.2f}.")
    else:
        print(f"You need {expected_gold_yield - real_gold_yield :.2f} gold.")
