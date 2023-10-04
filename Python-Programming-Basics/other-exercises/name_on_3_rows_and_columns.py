# Print your name in 3 rows and columns

name = input("What is your name: ")

for _ in range(5):
    for j in range(3):
        print(name, end=" ")
    print()
