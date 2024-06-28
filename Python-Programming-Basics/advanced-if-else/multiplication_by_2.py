# Multiplication by 2

result = 0

while True:

    result = float(input())
    if result < 0:
        print("Negative number!")
        break
    result *= 2
    print(f"Result: {result :.2f}")
