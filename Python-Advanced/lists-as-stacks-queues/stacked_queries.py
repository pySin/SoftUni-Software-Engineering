#  Stacked Queries


stack = []

n = int(input())


for i in range(n):
    command = input().split()

    if command[0] == "1":
        stack.append(int(command[1]))
    elif command[0] == "2":
        if stack:
            stack.pop()
    elif command[0] == "3":
        if stack:
            print(max(stack))
    elif command[0] == "4":
        if stack:
            print(min(stack))

print(", ".join([str(stack.pop()) for i in range(len(stack))]))
