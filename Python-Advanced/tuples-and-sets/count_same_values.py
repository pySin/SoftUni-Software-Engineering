# Count Same Values

values = tuple([float(num) for num in input().split()])
counted_numbers = []

for i in range(len(values)):
    if [values[i], values.count(values[i])] not in counted_numbers:
        counted_numbers.append([values[i], values.count(values[i])])

for item in counted_numbers:
    print(f"{item[0]} - {item[1]} times")
