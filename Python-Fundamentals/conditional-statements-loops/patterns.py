# Patterns

longest_line = int(input())

for i in range(longest_line + 1):
    longest_reached = 0
    for j in range(i):
        if j == longest_line - 1:
            longest_reached = j
        print("*", end="")
    print()

    if not longest_reached == 0:
        for k in range(longest_line - 1, 0, -1):
            for m in range(k):
                print("*", end="")
            print()

# for j in range(longest_line - 1, 0, -1):
#     print(j * "* ")
