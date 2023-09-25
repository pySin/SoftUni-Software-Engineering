# Sum Prime Non Prime

command = input()
prime_numbers_sum = 0
composite_numbers_sum = 0

is_composite = False
while command != "stop":
    current_number = int(command)
    if current_number < 0:
        print("Number is negative.")
        command = input()
        continue

    for divisor in range(2, current_number):
        if current_number % divisor == 0:
            composite_numbers_sum += current_number
            is_composite = True
            break

    if not is_composite:
        prime_numbers_sum += current_number
    is_composite = False

    command = input()

print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {composite_numbers_sum}")
