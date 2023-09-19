# Happy Numbers

raw_initial_number = int(input())
initial_number = raw_initial_number

if initial_number > 9:
    initial_number = 10

for i in range(1, initial_number):
    for j in range(1, initial_number):
        for h in range(1, initial_number):
            for k in range(1, initial_number):
                if i + j == h + k:
                    happy_number_string = str(i) + str(j) + str(h) + str(k)
                    first_sum = i + j
                    happy_number = int(happy_number_string)
                    if raw_initial_number % first_sum == 0:
                        print(str(i) + str(j) + str(h) + str(k), end=" ")
