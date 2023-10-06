# Print this using nested Loops

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

n = int(input("Enter star top number: "))

# for i in range(n):
#     print("* " * i)
#     if i == n - 1:
#         for j in range(i - 1, 0, -1):
#             print("* " * j)

for i in range(n):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
