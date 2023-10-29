# Battleships More exercises


def fleet():
    number_of_rows = int(input())

    fleet_of_ships = []

    for _ in range(number_of_rows):

        ship_row = [int(x) for x in input().split()]
        fleet_of_ships.append(ship_row)

    return fleet_of_ships


def attack(fleet_of_ships):
    attacked_coordinates = input().split()

    destroyed_ships = 0

    for hit in attacked_coordinates:
        hit_coordinate = [int(x) for x in hit.split("-")]
        if fleet_of_ships[hit_coordinate[0]][hit_coordinate[1]] != 0:
            fleet_of_ships[hit_coordinate[0]][hit_coordinate[1]] -= 1
            if fleet_of_ships[hit_coordinate[0]][hit_coordinate[1]] == 0:
                destroyed_ships += 1
    return destroyed_ships


def call_functions():
    fleet_of_ships = fleet()
    destroyed_ships = attack(fleet_of_ships)
    print(destroyed_ships)


if __name__ == "__main__":
    call_functions()
