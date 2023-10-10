# Evaluate Floating Point Number

number_float = float(input())

if number_float == 0:
    print("zero")
elif number_float > 0:
    if number_float < 1:
        print("small positive")
    elif number_float > 1000000:
        print("large positive")
    else:
        print("positive")
else:
    if number_float > -1:
        print("small negative")
    elif number_float < -1000000:
        print("large negative")
    else:
        print("negative")
