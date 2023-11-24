# A miner task


def miners_task():

    resources = {}

    key = None
    value = None

    line = 0
    while True:
        line += 1
        command = input()
        if command == "stop":
            break

        if line % 2 == 0:
            amount = int(command)
            value = amount
        else:
            key = command
            continue

        if key in resources.keys():
            resources[key] += value
        else:
            resources[key] = value

    return resources


for resource, amount in miners_task().items():
    print(f"{resource} -> {amount}")
