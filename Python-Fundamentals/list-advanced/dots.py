# Dots


def create_board():
    number_of_rows = int(input())

    board = []

    for _ in range(number_of_rows):
        row = input().split()
        board.append(row)
    return board


def find_dot(board):
    link_lengths = []
    dots_checked = []

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == ".":
                if [r, c] not in dots_checked:
                    linked_dots, dots_checked = check_link(board, [r, c], dots_checked)
                    link_lengths.append(linked_dots)
                else:
                    continue
    return link_lengths, dots_checked


def check_link(board, dot, dots_checked):

    current_links = [dot]
    linked_dots = 0

    while True:
        coordinates = current_links[0]
        row = coordinates[0]
        column = coordinates[1]

        # print(row)
        # print(column)

        is_dot_found = False

        # Upper position
        if row != 0:
            if board[row - 1][column] == ".":
                if [row - 1, column] not in dots_checked and [row - 1, column] not in current_links:
                    current_links.append([row - 1, column])
                    is_dot_found = True

        # Right position
        if column != len(board[0]) - 1:
            # print(f"Column length {len(board[0])}")
            # print(f"Index {str(row)}, {column})")
            if board[row][column + 1] == ".":
                if [row, column + 1] not in dots_checked and [row, column + 1] not in current_links:
                    current_links.append([row, column + 1])
                    is_dot_found = True

        # Lower position
        if row != len(board) - 1:
            if board[row + 1][column] == ".":
                if [row + 1, column] not in dots_checked and [row + 1, column] not in current_links:
                    current_links.append([row + 1, column])
                    is_dot_found = True

        # Left position
        if column != 0:
            if board[row][column - 1] == ".":
                if [row, column - 1] not in dots_checked and [row, column - 1] not in current_links:
                    current_links.append([row, column - 1])
                    is_dot_found = True

        if not is_dot_found:
            dots_checked.append(current_links.pop(0))
            linked_dots += 1

        if len(current_links) < 1:
            break

    # print(linked_dots)
    return linked_dots, dots_checked


def call_functions():
    board = create_board()
    data = find_dot(board)
    if len(data[0]) > 0:
        print(max(data[0]))
    else:
        print(0)


if __name__ == "__main__":
    call_functions()
