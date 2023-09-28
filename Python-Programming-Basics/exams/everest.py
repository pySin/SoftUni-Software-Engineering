# Everest

height_reached = 5364
GOAL_HEIGHT = 8848
days_passed = 0

is_fail = False
while height_reached < GOAL_HEIGHT:

    resting = input()
    if resting == "END":
        is_fail = True
        break

    if resting == "Yes":
        days_passed += 1
    elif resting == "No" and days_passed == 0:
        pass
    else:
        days_passed += 1

    day_meters_climbed = int(input())

    height_reached += day_meters_climbed
    if days_passed == 5:
        is_fail = True
        break


if is_fail:
    print("Failed!")
    print(height_reached)
else:
    print(f"Goal reached for {days_passed} days!")
