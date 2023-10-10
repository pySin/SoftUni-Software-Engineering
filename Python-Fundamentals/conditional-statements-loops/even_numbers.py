# Even Numbers

numbers_count = int(input())

is_odd = False
for i in range(numbers_count):
    current_number = int(input())
    if not current_number % 2 == 0:
        print(f"{current_number} is odd!")
        is_odd = True
        break

if not is_odd:
    print("All numbers are even.")
