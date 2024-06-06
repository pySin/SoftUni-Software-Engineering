# Prime Numbers


def get_primes(numbers: list):
    for number in numbers:
        if number < 2:
            continue
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            yield number


print(get_primes([2, 4, 3, 5, 6, 9, 1, 0]))
print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))

for item in get_primes([2, 4, 3, 5, 6, 9, 1, 0]):
    print(item)
