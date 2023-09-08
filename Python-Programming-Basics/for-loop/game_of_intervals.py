# Game of intervals

# Първи ред - колко хода ще има по време на играта – цяло число в интервала [1...100]
# За всеки ход – числата, които се проверяват в кой интервал са – цели числа в интервала [-100...100]

turns_count = int(input())
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid_numbers = 0

result = 0

for _ in range(turns_count):
    current_number = int(input())

    if 0 <= current_number < 10:
        from_0_to_9 += 1
        result += current_number * 0.20
    elif 10 <= current_number < 20:
        from_10_to_19 += 1
        result += current_number * 0.30
    elif 20 <= current_number < 30:
        from_20_to_29 += 1
        result += current_number * 0.40
    elif 30 <= current_number < 40:
        from_30_to_39 += 1
        result += 50
    elif 40 <= current_number <= 50:
        from_40_to_50 += 1
        result += 100
    else:
        result *= 0.50
        invalid_numbers += 1


print(f"{result :.2f}")
print(f"From 0 to 9: {(from_0_to_9 / turns_count) * 100 :.2f}%")
print(f"From 10 to 19: {(from_10_to_19 / turns_count) * 100 :.2f}%")
print(f"From 20 to 29: {(from_20_to_29 / turns_count) * 100 :.2f}%")
print(f"From 30 to 39: {(from_30_to_39 / turns_count) * 100 :.2f}%")
print(f"From 40 to 50: {(from_40_to_50 / turns_count) * 100 :.2f}%")
print(f"Invalid numbers: {(invalid_numbers / turns_count) * 100 :.2f}%")
