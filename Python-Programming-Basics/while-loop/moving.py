# Moving

length_free_space = int(input())
width_free_space = int(input())
height_free_space = int(input())

cubic_free_space = length_free_space * width_free_space * height_free_space

is_space_enough = False
while cubic_free_space > 0:

    boxes_to_move = 0
    boxes = input()
    if boxes == "Done":
        is_space_enough = True
        break
    else:
        boxes_to_move = int(boxes)

    cubic_free_space -= boxes_to_move

if is_space_enough:
    print(f"{cubic_free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(cubic_free_space)} Cubic meters more.")
