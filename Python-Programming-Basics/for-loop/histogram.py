# Histogram

number_of_numbers = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

full_count = 0

for _ in range(number_of_numbers):
    current_number = int(input())

    if current_number < 200:
        full_count += 1
        p1 += 1
    if 200 <= current_number < 400:
        full_count += 1
        p2 += 1

    if 400 <= current_number < 600:
        full_count += 1
        p3 += 1

    if 600 <= current_number < 800:
        full_count += 1
        p4 += 1

    if current_number >= 800:
        full_count += 1
        p5 += 1

print(f"{(p1 / full_count) * 100 :.2f}%")
print(f"{(p2 / full_count) * 100 :.2f}%")
print(f"{(p3 / full_count) * 100 :.2f}%")
print(f"{(p4 / full_count) * 100 :.2f}%")
print(f"{(p5 / full_count) * 100 :.2f}%")
