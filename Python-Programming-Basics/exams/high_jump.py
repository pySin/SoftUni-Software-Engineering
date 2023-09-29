# High Jump

# На първия ред се прочита желаната от Тихомир Иванов височина в сантиметри
# На всеки следващ ред до приключване на програмата се прочита височината от скока на Иванов

height = int(input())
starting_height = height - 30
unsuccessful_jump = 0
current_height = 0

x = 0
while True:

    if unsuccessful_jump == 3:
        print(f"Tihomir failed at {starting_height}cm after {x} jumps.")
        break

    x += 1
    current_height = int(input())

    if current_height > height:
        print(f"Tihomir succeeded, he jumped over {starting_height}cm after {x} jumps.")
        break

    if current_height > starting_height:
        starting_height += 5
        unsuccessful_jump = 0
    elif current_height <= starting_height:
        unsuccessful_jump += 1
