# List Statistics

number_of_items = int(input())

positive_numbers = []
negative_numbers = []

for i in range(number_of_items):
    current_number = int(input())

    if current_number < 0:
        negative_numbers.append(current_number)
    else:
        positive_numbers.append(current_number)

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {len(positive_numbers)}")
print(f"Sum of negatives: {sum(negative_numbers)}")
