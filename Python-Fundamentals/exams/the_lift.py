#  The Lift

MAX_WAGON_CAPACITY = 4


def queue_wagon_state():
    people_on_queue = int(input())
    lift_wagons = [int(wagon) for wagon in input().split()]
    return people_on_queue, lift_wagons


def fill_wagons(people_queue, wagons_state):

    for wagon in wagons_state:
        if wagon + people_queue <= MAX_WAGON_CAPACITY:
            wagons_state[wagons_state.index(wagon)] = wagon + people_queue
            people_queue = 0
            break
        else:
            people_queue -= MAX_WAGON_CAPACITY - wagons_state[wagons_state.index(wagon)]
            wagons_state[wagons_state.index(wagon)] = MAX_WAGON_CAPACITY

    return people_queue, wagons_state


def call_functions():
    queue, lift_wagons = queue_wagon_state()
    queue, lift_wagons = fill_wagons(queue, lift_wagons)

    if queue > 0:
        print(f"There isn't enough space! {queue} people in a queue!")
        print(" ".join([str(num) for num in lift_wagons]))
    elif queue == 0:
        if sum(lift_wagons) == len(lift_wagons) * MAX_WAGON_CAPACITY:
            print(" ".join([str(num) for num in lift_wagons]))
        else:
            print("The lift has empty spots!")
            print(" ".join([str(num) for num in lift_wagons]))


if __name__ == "__main__":
    call_functions()
