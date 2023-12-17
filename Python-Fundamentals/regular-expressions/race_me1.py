# Race
import re


def extract_name(sequence):
    pattern = r"[A-Za-z]"
    name = re.findall(pattern, sequence)
    return "".join(name)


def extract_numbers(sequence):
    pattern = r"[0-9]"
    numbers = re.findall(pattern, sequence)
    return sum([int(num) for num in numbers])


def order_players(personal_scores):
    return sorted(personal_scores, key=lambda x: personal_scores[x], reverse=True)


def filter_scores(ordered_scores):
    return ordered_scores[:3]


def call_functions():
    names = input().split(", ")
    personal_scores = {}

    command = input()
    while command != "end of race":
        name = extract_name(command)
        person_score = extract_numbers(command)
        if name in names:
            if name in personal_scores:
                personal_scores[name] += person_score
            else:
                personal_scores[name] = person_score

        command = input()
    ordered_scores = order_players(personal_scores)
    filtered_scores = filter_scores(ordered_scores)
    print(f"1st place: {filtered_scores[0]}")
    print(f"2nd place: {filtered_scores[1]}")
    print(f"3rd place: {filtered_scores[2]}")


if __name__ == "__main__":
    call_functions()
