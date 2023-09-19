# Combinations

n = int(input())

combinations = 0
x = 0
while x < n + 1:
    y = 0
    while y < n + 1:
        z = 0
        while z < n + 1:
            if x + y + z == n:
                combinations += 1
            z += 1
        y += 1
    x += 1
print(combinations)
