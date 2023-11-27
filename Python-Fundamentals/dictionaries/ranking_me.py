# Ranking


def add_contest_option(contest, password, contest_options):
    contest_options[contest] = password
    return contest_options


def order_contest_results(contest_results):

    top_contestant = [[name, sum(contest_results[name].values())] for name in contest_results]
    best_candidate, score = sorted(top_contestant, key=lambda x: x[1])[-1]
    print(f"Best candidate is {best_candidate} with total {score} points.")
    print("Ranking:")
    for contestant in sorted(contest_results):
        print(contestant)
        for key, value in sorted(contest_results[contestant].items(), key=lambda x: x[1], reverse=True):
            print(f"#  {key} -> {value}")


def function_call():

    contest_options = {}
    command = input().split(":")

    while command[0] != "end of contests":
        contest = command[0]
        contest_password = command[1]

        contest_options = add_contest_option(contest, contest_password, contest_options)
        command = input().split(":")

    contest_results = {}
    command = input().split("=>")

    while command[0] != "end of submissions":
        subject = command[0]
        password = command[1]
        name = command[2]
        points = int(command[3])

        if subject in contest_options:
            if contest_options[subject] == password:
                if name in contest_results:
                    if subject in contest_results[name]:
                        if points > contest_results[name][subject]:
                            contest_results[name][subject] = points
                    else:
                        contest_results[name][subject] = points
                else:
                    contest_results[name] = {subject: points}
        command = input().split("=>")

    order_contest_results(contest_results)


if __name__ == "__main__":
    function_call()
