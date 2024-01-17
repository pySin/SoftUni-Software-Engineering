# World Tour


def initial_stops():
    stops = input()
    return stops


def add_destination(stops, instruction):
    index = int(instruction[1])
    if abs(index) < len(stops):
        stops = stops[:index] + instruction[2] + stops[index:]
    print(stops)
    return stops


def remove_destination(stops, instructions):
    start_cut = int(instructions[1])
    end_cut = int(instructions[2])
    if abs(start_cut) < len(stops) and abs(end_cut) < len(stops):
        stops = stops[:start_cut] + stops[end_cut + 1:]
    print(stops)
    return stops


def switch_destination(stops, instruction):
    old_destination = instruction[1]
    new_destination = instruction[2]
    stops = stops.replace(old_destination, new_destination)
    print(stops)
    return stops


def call_function():
    stops = initial_stops()
    command = input()

    while command != "Travel":

        instruction = command.split(":")

        if "Add" in instruction[0]:
            stops = add_destination(stops, instruction)
        elif "Remove" in instruction[0]:
            stops = remove_destination(stops, instruction)
        elif instruction[0] == "Switch":
            stops = switch_destination(stops, instruction)

        command = input()
    print(f"Ready for world tour! Planned stops: {stops}")


if __name__ == "__main__":
    call_function()
