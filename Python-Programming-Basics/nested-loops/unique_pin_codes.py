# Unique Pin Codes

first_number_limit = int(input())
second_number_limit = int(input())
third_number_limit = int(input())

for i in range(1, first_number_limit + 1):
    for j in range(1, second_number_limit + 1):
        for h in range(1, third_number_limit + 1):
            if i % 2 == 0 and h % 2 == 0 and 1 < j < 8:
                if j == 2 or j % 2 != 0:
                    # print(str(i) + " " + str(j) + " " + str(h))
                    print(i, end=" ")
                    print(j, end=" ")
                    print(h)
