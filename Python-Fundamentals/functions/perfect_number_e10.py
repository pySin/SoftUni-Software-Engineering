# Perfect Number

def perfect_number(main_number: int) -> str:
    divisors_collection = []
    for divisor in range(1, (main_number // 2) + 1):
        if main_number % divisor == 0:
            divisors_collection.append(divisor)

    # print(divisors_collection)
    if sum(divisors_collection) == main_number:
        return "We have a perfect number!"
    else:
        return "It\'s not so perfect."


number = int(input())
print(perfect_number(number))
