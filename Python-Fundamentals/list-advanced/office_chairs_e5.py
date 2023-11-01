# Office Chairs


rooms_count_get = int(input())


def office_chairs(rooms_count):
    is_chairs_insufficient = False
    chairs_left = 0
    messages = []

    for chairs in range(rooms_count):
        chairs_per_room = input().split(" ")
        if len(chairs_per_room[0]) < int(chairs_per_room[1]):
            messages.append(f"{int(chairs_per_room[1]) - len(chairs_per_room[0]) } "
                            f"more chairs needed in room {chairs + 1}")
            is_chairs_insufficient = True
        else:
            chairs_left += len(chairs_per_room[0]) - int(chairs_per_room[1])

    if is_chairs_insufficient:
        return messages
    else:
        return [f"Game On, {chairs_left} free chairs left"]


for message in office_chairs(rooms_count_get):
    print(message)
