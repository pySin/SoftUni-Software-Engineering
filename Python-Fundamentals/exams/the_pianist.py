# The Pianist


def make_initial_collection(number_of_pieces):
    pieces_collection = {}
    for _ in range(number_of_pieces):
        piece, composer, key = input().split("|")
        pieces_collection[piece] = [composer, key]
    return pieces_collection


def change_collection(pieces_collection):

    command = input()

    while command != "Stop":
        instruction = command.split("|")
        action = instruction[0]

        if action == "Add":
            piece = instruction[1]
            composer = instruction[2]
            key = instruction[3]

            if piece not in pieces_collection:
                pieces_collection[piece] = [composer, key]
                print(f"{piece} by {composer} in {key} added to the collection!")
            else:
                print(f"{piece} is already in the collection!")
        elif action == "Remove":
            piece = instruction[1]

            if piece in pieces_collection:
                pieces_collection.pop(piece)
                print(f"Successfully removed {piece}!")
            else:
                print(f"Invalid operation! {piece} does not exist in the collection.")
        elif action == "ChangeKey":
            piece = instruction[1]
            new_key = instruction[2]

            if piece in pieces_collection:
                pieces_collection[piece][1] = new_key
                print(f"Changed the key of {piece} to {new_key}!")
            else:
                print(f"Invalid operation! {piece} does not exist in the collection.")
        command = input()

    return pieces_collection


def display_collection(pieces_collection):
    for record in pieces_collection:
        piece = record
        composer = pieces_collection[record][0]
        key = pieces_collection[record][1]
        print(f"{piece} -> Composer: {composer}, Key: {key}")


def call_functions():
    number_of_pieces = int(input())
    pieces_collection = make_initial_collection(number_of_pieces)
    pieces_collection = change_collection(pieces_collection)
    display_collection(pieces_collection)


if __name__ == "__main__":
    call_functions()
