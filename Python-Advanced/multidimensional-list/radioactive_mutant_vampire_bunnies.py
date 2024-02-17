# Radioactive Mutant Vampire Bunnies


def create_matrix(rows: int) -> list:
    matrix = [[char for char in list(input())] for _ in range(rows)]
    return matrix


def check_borders(rows: int, cols: int) -> bool:
    pass


def player_move(matrix: list, move: str, player_row: int, player_coll: int):
    moves = {
        "L": lambda x, y: False if not 0 <= (y - 1) else (x, y - 1),
        "R": lambda x, y: False if not (y + 1) < len(matrix[0]) else (x, y + 1),
        "U": lambda x, y: False if not 0 <= (x - 1) else (x - 1, y),
        "D": lambda x, y: False if not (x + 1) < len(matrix) else (x + 1, y)
    }

    out_or_coordinates = moves[move](player_row, player_coll)

    moves_on_bunny = {
        "L": lambda x, y: True if matrix[x][y - 1] == "B" else False,
        "R": lambda x, y: True if matrix[x][y + 1] == "B" else False,
        "U": lambda x, y: True if matrix[x - 1][y] == "B" else False,
        "D": lambda x, y: True if matrix[x + 1][y] == "B" else False
    }

    bunny = moves_on_bunny[move](player_row, player_coll)
    return out_or_coordinates, bunny


def bunny_population(matrix: list):

    spread_bunny = {
        "up": lambda x, y: True if 0 <= (x - 1) else False,
        "down": lambda x, y: True if (x + 1) < len(matrix) else False,
        "left": lambda x, y: True if 0 <= (y - 1) else False,
        "right": lambda x, y: True if (y + 1) < len(matrix[0]) else False
    }

    current_bunnies = [[[i, j] for j in range(len(matrix[0])) if matrix[i][j] == "B"] for i in range(len(matrix))]
    current_bunnies = [x for x in current_bunnies if len(x) > 0]
    current_bunnies = [position for sublist in current_bunnies for position in sublist]
    print(f"current bunnies: {current_bunnies}")

    return matrix


def call_functions():
    rows, cols = [int(x) for x in input().split()]
    matrix = create_matrix(rows)
    print(matrix)
    player_row, player_coll = [[[r, c] for c in range(cols) if matrix[r][c] == "P"] for r
                               in range(rows) if "P" in matrix[r]][0][0]
    print(player_row, player_coll)
    moves = list(input())
    for move in moves:
        out, bunny = player_move(matrix, move, player_row, player_coll)
        print(out, bunny)
        if not out:
            print(f"won: {player_row} {player_coll}")
            break
        elif bunny:
            print(f"dead: {player_row} {player_coll}")
            break
        else:
            player_row, player_coll = out
            matrix = bunny_population(matrix)
            print(matrix)

        if not matrix[0]:
            print("GAME OVER")
            break
    print("Out of breaks!")


if __name__ == "__main__":
    call_functions()
