# Radioactive Mutant Vampire Bunnies


def create_matrix(rows: int) -> list:
    matrix = [[char for char in list(input())] for _ in range(rows)]
    return matrix


def is_move_out(matrix: list, move: str, player_row: int, player_coll: int):
    moves = {
        "L": lambda x, y: (x, y - 1) if 0 <= (y - 1) else False,
        "R": lambda x, y: (x, y + 1) if (y + 1) < len(matrix[0]) else False,
        "U": lambda x, y: (x - 1, y) if 0 <= (x - 1) else False,
        "D": lambda x, y: (x + 1, y) if (x + 1) < len(matrix) else False
    }

    return moves[move](player_row, player_coll)


def is_move_bunny(matrix: list, move: str, player_row: int, player_coll: int):
    moves = {
        "L": lambda x, y: False if matrix[x][y - 1] == "B" else True,
        "R": lambda x, y: False if matrix[x][y + 1] == "B" else True,
        "U": lambda x, y: False if matrix[x - 1][y] == "B" else True,
        "D": lambda x, y: False if matrix[x + 1][y] == "B" else True
    }

    return moves[move](player_row, player_coll)


def bunny_population(matrix: list, player_row: int, player_coll: int):
    current_bunnies = [[[i, j] for j in range(len(matrix[0])) if matrix[i][j] == "B"] for i in range(len(matrix))]
    current_bunnies = [x for x in current_bunnies if len(x) > 0]
    current_bunnies = [position for sublist in current_bunnies for position in sublist]

    is_player_dead = False
    for bunny in current_bunnies:
        if is_move_out(matrix, "L", bunny[0], bunny[1]):
            if bunny[0] == player_row and bunny[1] - 1 == player_coll:
                is_player_dead = True
            matrix[bunny[0]][bunny[1] - 1] = "B"
        if is_move_out(matrix, "R", bunny[0], bunny[1]):
            if bunny[0] == player_row and bunny[1] + 1 == player_coll:
                is_player_dead = True
            matrix[bunny[0]][bunny[1] + 1] = "B"
        if is_move_out(matrix, "U", bunny[0], bunny[1]):
            if bunny[0] - 1 == player_row and bunny[1] == player_coll:
                is_player_dead = True
            matrix[bunny[0] - 1][bunny[1]] = "B"
        if is_move_out(matrix, "D", bunny[0], bunny[1]):
            if bunny[0] + 1 == player_row and bunny[1] == player_coll:
                is_player_dead = True
            matrix[bunny[0] + 1][bunny[1]] = "B"
    return matrix, is_player_dead


def call_functions():
    rows, cols = [int(x) for x in input().split()]
    matrix = create_matrix(rows)
    player_row, player_coll = [[[r, c] for c in range(cols) if matrix[r][c] == "P"] for r
                               in range(rows) if "P" in matrix[r]][0][0]
    matrix[player_row][player_coll] = "."
    moves = list(input())
    for move in moves:
        coordinates_or_out = is_move_out(matrix, move, player_row, player_coll)
        if coordinates_or_out:
            true_or_bunny = is_move_bunny(matrix, move, player_row, player_coll)
            if true_or_bunny:
                player_row, player_coll = coordinates_or_out
            else:
                matrix, is_player_dead = bunny_population(matrix, player_row, player_coll)
                if move == "L":
                    player_coll -= 1
                elif move == "R":
                    player_coll += 1
                elif move == "U":
                    player_row -= 1
                elif move == "D":
                    player_row += 1
                # print("JUMP ON BUNNY")
                [print("".join(row)) for row in matrix]
                print(f"dead: {player_row} {player_coll}")
                break
        else:
            matrix, is_player_dead = bunny_population(matrix, player_row, player_coll)
            [print("".join(row)) for row in matrix]
            print(f"won: {player_row} {player_coll}")
            break

        matrix, is_player_dead = bunny_population(matrix, player_row, player_coll)
        if is_player_dead:
            [print("".join(row)) for row in matrix]
            print(f"dead: {player_row} {player_coll}")
            break


if __name__ == "__main__":
    call_functions()
