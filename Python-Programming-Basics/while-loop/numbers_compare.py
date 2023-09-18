# Numbers Compare

initial_number = int(input())
sum_numbers = 0
# check_number = 0
while not sum_numbers >= initial_number:
    check_number = int(input())
    sum_numbers += check_number

print(f"{sum_numbers}")
