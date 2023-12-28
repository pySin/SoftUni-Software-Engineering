# Winning Ticket


def lottery(ticket):

    if len(ticket) != 20:
        return "invalid ticket"

    first_half = ticket[0:10]
    second_half = ticket[10:20]

    win_row_1 = ""
    win_count_1 = 0

    win_row_2 = ""
    win_count_2 = 0
    for winning_symbol in "@#$^":
        for i in range(len(first_half)):
            if first_half[i] == winning_symbol:
                win_row_1 += winning_symbol
                if len(win_row_1) >= 6:
                    win_count_1 = len(win_row_1)
            else:
                if win_count_1 >= 6:
                    break

        for i in range(len(second_half)):
            if second_half[i] == winning_symbol:
                win_row_2 += winning_symbol
                if len(win_row_2) >= 6:
                    win_count_2 = len(win_row_2)
            else:
                if win_count_2 >= 6:
                    break

        if win_count_1 < win_count_2:
            winning_count = win_count_1
        else:
            winning_count = win_count_2

        if winning_count == 10:
            return f"ticket \"{ticket}\" - {winning_count}{winning_symbol} Jackpot!"

        if winning_count >= 6:
            # if second_half.count(winning_symbol) == winning_count:
            return f"ticket \"{ticket}\" - {winning_count}{winning_symbol}"

    return f"ticket \"{ticket}\" - no match"


if __name__ == "__main__":
    row = input().replace(" ", "")
    rows = row.split(",")
    for row in rows:
        print(lottery(row))

