# Rounding

def rounding(num_row):
    num_row = num_row.split(" ")
    num_row = list(map(round, map(float, num_row)))
    return num_row


numbers_row = input()
print(rounding(numbers_row))
