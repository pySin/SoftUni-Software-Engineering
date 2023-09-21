# Number Pyramid

n = int(input())

increase = 1
is_limit_reached = False
for row in range(1, n + 1):
    for col in range(increase, increase + row):
        print(col, end=" ")
        if col == n:
            is_limit_reached = True
            break
    if is_limit_reached:
        break
    print()
    increase += row
