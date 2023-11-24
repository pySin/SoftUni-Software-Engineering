# Judge


def get_and_structure():
    command = input().split(" -> ")

    contest_scores = {}

    while command[0] != "no more time":

        name, contest, points = command
        if contest not in contest_scores:
            contest_scores[contest] = [[name, int(points)]]
        else:
            if name not in [x[0] for x in contest_scores[contest]]:
                contest_scores[contest].append([name, int(points)])
            for i in range(len(contest_scores[contest])):
                if contest_scores[contest][i][0] == name and contest_scores[contest][i][1] < int(points):
                    contest_scores[contest][i][1] = int(points)

        command = input().split(" -> ")
    return contest_scores


def order_data(data):

    for contest in data:
        data[contest] = sorted(data[contest], key=lambda x: x[0])
        data[contest] = sorted(data[contest], key=lambda x: x[1], reverse=True)

    for contest_name in data:
        print(f"{contest_name}: {len(data[contest_name])} participants")
        for i in range(len(data[contest_name])):
            print(f"{i + 1}. {data[contest_name][i][0]} <::> {data[contest_name][i][1]}")
    return data


def individual_results(data):
    individual_points = {}
    for contest in data:
        for name, points in data[contest]:
            if name not in individual_points:
                individual_points[name] = int(points)
            else:
                individual_points[name] += int(points)
    individual_points = sorted(individual_points.items(), key=lambda x: x[0])
    # print(individual_points)
    individual_points = sorted(individual_points, key=lambda x: x[1], reverse=True)
    print("Individual standings:")
    for i in range(len(individual_points)):
        print(f"{i + 1}. {individual_points[i][0]} -> {individual_points[i][1]}")
    # print(individual_points)


def call_functions():
    judge_data = get_and_structure()
    ordered_data = order_data(judge_data)
    # print(ordered_data)
    individual_results(ordered_data)


if __name__ == "__main__":
    call_functions()
