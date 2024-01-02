# Destination Mapper
import re


def find_destinations(destinations):
    pattern = r"(/|=)([A-Z][a-zA-Z]{2,})\1"
    result = re.findall(pattern, destinations)
    return result


def extract_destinations(destinations):
    destinations = [destination[1] for destination in destinations]
    return destinations


def travel_points_calculate(destinations):
    travel_points = len("".join(destinations))
    return travel_points


def call_functions():
    destinations_text = input()
    destinations = find_destinations(destinations_text)
    destinations = extract_destinations(destinations)
    print(f"Destinations: {', '.join(destinations)}")
    travel_points = travel_points_calculate(destinations)
    print(f"Travel Points: {travel_points}")


if __name__ == "__main__":
    call_functions()
