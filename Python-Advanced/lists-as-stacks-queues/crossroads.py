# Crossroads
from collections import deque


def current_crossing(car_queue: deque, green_l: int, free_w: int):
    cars_passed = 0
    while car_queue:
        if green_l == 0:
            # cars_passed += 1
            return False, car_queue, cars_passed
        car = car_queue.popleft()
        current_car = car
        car = deque(car)
        while car:
            car.popleft()
            if green_l == 0:
                free_w -= 1
                if free_w == 0 and car:
                    character_hit = car.popleft()
                    print("A crash happened!")
                    print(f"{current_car} was hit at {character_hit}.")
                    return True, car_queue, 0
            else:
                green_l -= 1
        cars_passed += 1
    return False, car_queue, cars_passed


def command_handle(command, car_queue, green_l, free_w):
    is_crash = False
    if command != "green":
        car_queue.append(command)
        return is_crash, car_queue, 0
    else:
        is_crash, car_queue, cars_passed = current_crossing(car_queue, green_l, free_w)
    return is_crash, car_queue, cars_passed


def crossing():
    green_light = int(input())
    free_window = int(input())

    all_cars_passed = 0
    command = input()
    car_queue = deque()
    is_crash = False
    while command != "END":
        is_crash, car_queue, cars_passed = command_handle(command, car_queue, green_light, free_window)
        if is_crash:
            break
        all_cars_passed += cars_passed

        command = input()
    if not is_crash:
        print("Everyone is safe.")
        print(f"{all_cars_passed} total cars passed the crossroads.")


if __name__ == "__main__":
    crossing()
