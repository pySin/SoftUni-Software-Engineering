# Flatten Lists


def call_functions():
    lists = [[int(num) for num in row.split()] for row in input().split("|")][::-1]
    lists = [number for sublist in lists for number in sublist]
    print(*lists)


if __name__ == "__main__":
    call_functions()
