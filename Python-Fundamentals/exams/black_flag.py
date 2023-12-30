# Black Flag


days_of_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())


plunder_gained = 0
for i in range(1, days_of_plunder + 1):

    plunder_gained += daily_plunder

    if i % 3 == 0:
        plunder_gained += daily_plunder * 0.5

    if i % 5 == 0:
        plunder_gained *= 0.7

if plunder_gained >= expected_plunder:
    print(f"Ahoy! {plunder_gained:.2f} plunder gained.")
else:
    print(f"Collected only {(plunder_gained / expected_plunder) * 100:.2f}% of the plunder.")
