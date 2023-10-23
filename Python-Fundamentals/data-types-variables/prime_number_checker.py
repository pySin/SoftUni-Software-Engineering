# Prime Number Checker


number = int(input())

# Check first the smallest possible divisor 2 and later the others
divider = number // 2
prime_number = False

while True:

    if number in [2, 3]:
        prime_number = True
        break

    if divider == 1:
        prime_number = True

    if number % divider == 0:
        break

    divider -= 1


print(prime_number)
