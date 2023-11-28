# SoftUni Parking


def register_parking_user(user, plate_number, parking_data):
    if user in parking_data:
        print(f"ERROR: already registered with plate number {parking_data[user]}")
    else:
        parking_data[user] = plate_number
        print(f"{user} registered {plate_number} successfully")

    return parking_data


def unregister_parking_user(user, parking_data):
    if user not in parking_data:
        print(f"ERROR: user {user} not found")
    else:
        del parking_data[user]
        print(f"{user} unregistered successfully")
    return parking_data


def call_functions():
    parking_data = {}

    n = int(input())

    for _ in range(n):
        command = input().split()
        action = command[0]
        user = command[1]

        if action == "register":
            plate_number = command[2]
            parking_data = register_parking_user(user, plate_number, parking_data)
        elif action == "unregister":
            parking_data = unregister_parking_user(user, parking_data)
    for user, plate in parking_data.items():
        print(f"{user} => {plate}")


if __name__ == "__main__":
    call_functions()
