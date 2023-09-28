# Everest 2

STARTING_HEIGHT = 5364
DESTINATION_HEIGHT = 8848
current_day = 0
current_height = 5364

command = input()
is_climbed_successful = False
while not command == "END":

    if command == "No" and current_day == 1:
        pass
    else:
        current_day += 1

    if current_day == 5:
        break

    day_climbed = int(input())
    current_height += day_climbed
    if current_height >= DESTINATION_HEIGHT:
        is_climbed_successful = True
        break

    command = input()

if is_climbed_successful:
    print(f"Goal reached for {current_day} days!")
else:
    print("Failed!")
    print(f"{current_height}")
