# The Lift
MAX_SIZE = 4

people_count = int(input())
lift_empty_spaces = input()


def fill_lift(people, cabins_spaces):
    cabins_spaces = list(map(int, cabins_spaces.split(" ")))
    for seats in range(len(cabins_spaces)):
        current_available_seats = MAX_SIZE - cabins_spaces[seats]
        if people < current_available_seats:
            cabins_spaces[seats] = people
            people = 0
            return "The lift has empty spots!", " ".join(map(str, cabins_spaces))
        else:
            cabins_spaces[seats] = MAX_SIZE
            people -= current_available_seats
    if people > 0:
        return f"There isn't enough space! {people} people in a queue!", " ".join(map(str, cabins_spaces))
    else:
        return " ".join(map(str, cabins_spaces))


if __name__ == "__main__":
    cabin_allocations = fill_lift(people_count, lift_empty_spaces)
    for phrase in cabin_allocations:
        print(phrase)
