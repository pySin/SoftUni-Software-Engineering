# Building Rooms Descending

floors = int(input())
rooms_per_floor = int(input())


for floor in range(floors, 0, -1):

    for room in range(rooms_per_floor):
        if floor == floors:
            if room == rooms_per_floor - 1:
                print(f"L{floor}{room}")
            else:
                print(f"L{floor}{room}", end=" ")

        elif floor % 2 == 0:
            if room == rooms_per_floor - 1:
                print(f"O{floor}{room}")
            else:
                print(f"O{floor}{room}", end=" ")
        else:
            if room == rooms_per_floor - 1:
                print(f"A{floor}{room}")
            else:
                print(f"A{floor}{room}", end=" ")
