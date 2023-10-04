# Letter Exercises

value = 65

for i in range(6):
    for j in range(i):
        print(chr(value), end=" ")
        value += 1
    print()
