# High Jump

# На първия ред се прочита желаната от Тихомир Иванов височина в сантиметри
# На всеки следващ ред до приключване на програмата се прочита височината от скока на Иванов

height = int(input())
INCREASE = 5
current_height = height - 30
command = int(input())

all_jumps = 1
is_practice_fail = False

height_changes = 0
while command <= height:
    current_jump = command
    current_height = (height - 30) + (INCREASE * height_changes)
    # print(f"Current height: {current_height}")

    height_changes += 1
    jumps_count = 0
    while current_jump <= current_height:
        jumps_count += 1
        # print(jumps_count)
        if jumps_count == 3:
            is_practice_fail = True
            break
        current_jump = int(input())
        all_jumps += 1

    if is_practice_fail:
        break
    command = int(input())
    all_jumps += 1
    # jumps_count = 1

if is_practice_fail:
    print(f"Tihomir failed at {current_height}cm "
          f"after {all_jumps} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {height}cm "
          f"after {all_jumps} jumps.")
