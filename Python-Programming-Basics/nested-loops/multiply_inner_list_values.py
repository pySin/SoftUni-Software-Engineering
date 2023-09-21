# Multiply Inner List Values

list_1 = [[1, 2], [3, 4]]
m = 1
for i in range(0, 2):
    m *= 10
    for j in range(0, 2):
        list_1[i][j] *= m
print(list_1)
