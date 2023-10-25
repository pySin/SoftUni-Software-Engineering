# Car Race


odd_number_sequence = input().split()
odd_number_sequence = [int(number) for number in odd_number_sequence]

steps_to_final = len(odd_number_sequence) // 2

left_player_result = 0
right_player_result = 0


for i in range(steps_to_final):
    if odd_number_sequence[i] == 0:
        left_player_result *= 0.8
    else:
        left_player_result += odd_number_sequence[i]

    if odd_number_sequence[len(odd_number_sequence) - (i + 1)] == 0:
        right_player_result *= 0.8
    else:
        right_player_result += odd_number_sequence[len(odd_number_sequence) - (i + 1)]

if left_player_result < right_player_result:
    print(f"The winner is left with total time: {left_player_result :.1f}")
else:
    print(f"The winner is right with total time: {right_player_result :.1f}")
