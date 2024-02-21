# Sum matrix Elements


rows, columns = [int(x) for x in input().split(", ")]
matrix = []

sums = 0
for row in range(rows):
    line = [int(x) for x in input().split(", ")]
    sums += sum(line)
    matrix.append(line)

print(sums)
print(matrix)
