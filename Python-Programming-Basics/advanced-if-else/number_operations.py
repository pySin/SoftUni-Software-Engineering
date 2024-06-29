# Number Operations

# ⦁	N1 - цяло число;
# ⦁	N2 - цяло число;
# ⦁	Оператор - един символ измежду: "+", "-", "*", "/", "%".

n1 = int(input())
n2 = int(input())
operator = input()  # "+", "-", "*", "/", "%"
even_odd = ""

if operator == "+":
    if (n1 + n2) % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{n1} {operator} {n2} = {n1 + n2} - {even_odd}")
elif operator == "-":
    if (n1 - n2) % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{n1} {operator} {n2} = {n1 - n2} - {even_odd}")
elif operator == "*":
    if (n1 * n2) % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{n1} {operator} {n2} = {n1 * n2} - {even_odd}")
elif operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f"{n1} / {n2} = {n1 / n2 :.2f}")
elif operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f"{n1} % {n2} = {n1 % n2}")
