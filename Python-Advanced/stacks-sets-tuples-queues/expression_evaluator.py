# Expression Evaluator
from collections import deque


calculation = deque([int(x) if x.lstrip("-").isdigit() else x for x in input().split()])
current_operation_digits = deque()

while True:

    symbol = calculation.popleft()
    if type(symbol) == int:
        current_operation_digits.append(symbol)
    else:
        operation_result = current_operation_digits.popleft()
        if symbol == "*":
            for i in current_operation_digits:
                operation_result *= i
        elif symbol == "+":
            for i in current_operation_digits:
                operation_result += i
        elif symbol == "-":
            for i in current_operation_digits:
                operation_result -= i
        elif symbol == "/":
            for i in current_operation_digits:
                operation_result //= i

        if len(calculation) == 0:
            calculation.appendleft(operation_result)
            break

        calculation.appendleft(operation_result)
        current_operation_digits = deque()

print(*calculation)

