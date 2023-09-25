# Special Numbers

base_number = int(input())

is_not_special = False
for i in range(1111, 10000):
    i_string = str(i)

    for j in range(len(i_string)):
        if int(i_string[j]) == 0:
            is_not_special = True
            break

        if base_number % int(i_string[j]) != 0:
            # print(str(base_number) + " % " + i_string[j])
            is_not_special = True
            break

    if not is_not_special:
        print(f"{i}", end=" ")
    is_not_special = False
