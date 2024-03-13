# Exit Founder

def create_matrix(rows_count: int):

    matrix_c = []
    for _ in range(rows_count):
        make_row = [r for r in input().split()]
        matrix_c.append(make_row)

    return matrix_c


player_1, player_2 = input().split(", ")
matrix = create_matrix(6)
current_player = player_1


position = input()
moves = 0
skip_moves = []
while position:
    moves += 1
    if moves in skip_moves:
        position = input()
        current_player = player_1 if current_player == player_2 else player_2
        continue

    row, col = [int(p) for p in position[1: -1].split(", ")]
    if matrix[row][col] == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break
    elif matrix[row][col] == "T":
        waiting_player = player_1 if current_player == player_2 else player_2
        print(f"{current_player} is out of the game! The winner is {waiting_player}.")
        break
    elif matrix[row][col] == "W":
        print(f"{current_player} hits a wall and needs to rest.")
        skip_moves.append(moves + 2)

    current_player = player_1 if current_player == player_2 else player_2
    position = input()
