# Kate's way out


def rows_maze():
    rows = int(input())
    maze = []

    for _ in range(rows):
        row = list(input())
        maze.append(row)
    return rows, maze


def initial_position(rows, maze):
    kate_row = [i for i in range(rows) if "k" in maze[i]][0]
    kate_column = [j for j in range(len(maze[0])) if maze[kate_row][j] == "k"][0]
    return [kate_row, kate_column, 0]


def next_moves(rows, maze, position, unfinished_positions):
    kate_row = position[0]
    kate_column = position[1]
    turns = position[2]

    one_exit = False
    while True:
        if kate_row == 0 or kate_row == rows - 1 or kate_column == 0 or kate_column == len(maze[1]) - 1:
            turns += 1
            one_exit = True
            # unfinished_positions = "Exit"
            break

        if maze[kate_row - 1][kate_column] == " ":
            if [kate_row, kate_column, turns] not in unfinished_positions:
                unfinished_positions.append([kate_row, kate_column, turns])
            kate_row = kate_row - 1
            maze[kate_row][kate_column] = "k"
            turns += 1

        elif maze[kate_row][kate_column + 1] == " ":
            if [kate_row, kate_column, turns] not in unfinished_positions:
                unfinished_positions.append([kate_row, kate_column, turns])
            kate_column = kate_column + 1
            maze[kate_row][kate_column] = "k"
            turns += 1

        elif maze[kate_row + 1][kate_column] == " ":
            if [kate_row, kate_column, turns] not in unfinished_positions:
                unfinished_positions.append([kate_row, kate_column, turns])
            kate_row = kate_row + 1
            maze[kate_row][kate_column] = "k"
            turns += 1

        elif maze[kate_row][kate_column - 1] == " ":
            kate_column = kate_column - 1
            maze[kate_row][kate_column] = "k"
            turns += 1
        else:
            if [kate_row, kate_column, turns] in unfinished_positions:
                unfinished_positions.remove([kate_row, kate_column, turns])
            break
    return maze, unfinished_positions, turns, one_exit


def call_functions():
    rows, maze = rows_maze()
    unfinished_positions = [initial_position(rows, maze)]
    # turns = 0
    # print(unfinished_positions)
    exits = []
    while True:
        maze, unfinished_positions, turns, one_exit = next_moves(rows, maze, unfinished_positions[0], unfinished_positions)

        # if unfinished_positions == "Exit":
        if one_exit:
            exits.append(turns)
            # print(f"Kate got out in {turns} moves")
            # break

        if len(unfinished_positions) < 1:
            # print(exits)
            # print("Kate cannot get out")
            break

    if len(exits) > 0:
        print(f"Kate got out in {max(exits)} moves")
    else:
        print("Kate cannot get out")


if __name__ == "__main__":
    call_functions()


# is_upper_wall = False
# is_lower_wall = False
#
# for i in range(len(maze)):
#     if " " not in maze[i] and i < kate_row:
#         is_upper_wall = True
#     elif " " not in maze[i] and i > kate_row:
#         is_lower_wall = True
#
#
# corridor_places = 0
#
# if not is_upper_wall and is_lower_wall:
#     for i in range(0, kate_row + 1):
#         for j in range(len(maze[i])):
#             if maze[i][j] == " ":
#                 corridor_places += 1
#
# if is_upper_wall and not is_lower_wall:
#     for i in range(kate_row, rows):
#         for j in range(len(maze[i])):
#             if maze[i][j] == " ":
#                 corridor_places += 1
#
# if is_upper_wall and is_lower_wall:
#     print("Kate cannot get out")
# else:
#     print(f"Kate got out in {corridor_places + 1} moves")
