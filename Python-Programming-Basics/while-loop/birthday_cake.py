# birthday cake

cake_width = int(input())
cake_height = int(input())

available_pieces = cake_width * cake_height

enough_pieces = False
while available_pieces > 0:
    current_pieces = input()  # STOP or integer as string!
    current_pieces_taken = 0

    if current_pieces == "STOP":
        enough_pieces = True
        break
    else:
        current_pieces_taken = int(current_pieces)

    available_pieces -= current_pieces_taken


if enough_pieces:
    print(f"{available_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(available_pieces)} pieces more.")
