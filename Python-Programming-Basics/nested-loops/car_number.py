# Car Number

lowest_number = int(input())
highest_number = int(input())

for i in range(lowest_number, highest_number + 1):
    for j in range(lowest_number, highest_number + 1):
        for h in range(lowest_number, highest_number + 1):
            for k in range(lowest_number, highest_number + 1):
                if i % 2 == 0 and k % 2 != 0 and i > k and (j + h) % 2 == 0:
                    print(i, end="")
                    print(j, end="")
                    print(h, end="")
                    print(k, end=" ")
                if i % 2 != 0 and k % 2 == 0 and i > k and (j + h) % 2 == 0:
                    print(i, end="")
                    print(j, end="")
                    print(h, end="")
                    print(k, end=" ")
