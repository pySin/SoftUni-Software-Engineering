# Print in 2 columns

phrase = "In the Old Palace Resort the holiday is going very well!"

is_long_enough = False
letter = 0
for i in range(len(phrase)):
    for j in range(3):
        if j % 2 == 0:
            print(phrase[letter], end=" ")
            letter += 1
            if letter == len(phrase):
                is_long_enough = True
                break
    if is_long_enough:
        break
    print()
