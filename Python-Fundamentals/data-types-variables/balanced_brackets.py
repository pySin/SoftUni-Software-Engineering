# Balanced Brackets


lines = int(input())
brackets = ""
expression = "UNBALANCED"

for i in range(lines):
    char = input()
    if char == "(":
        brackets += "("
    elif char == ")":
        brackets += ")"
    else:
        pass

    if brackets == ")":
        expression = "UNBALANCED"
        break
    elif brackets == "()":
        brackets = ""

if brackets == "":
    expression = "BALANCED"

print(expression)
