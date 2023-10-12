# Maximum Multiple

divisor = int(input())
boundary = int(input())

result = 0
for i in range(boundary, 0, -1):
    if i % divisor == 0:
        result = i
        break
print(result)
