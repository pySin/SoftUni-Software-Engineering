# # Balanced Parentheses
# from collections import deque
#
#
# def get_deque():
#     brackets = deque(input())
#     return brackets
#
#
# def check_balance():
#     parentheses = get_deque()
#
#     is_unbalanced = False
#     for _ in range(len(parentheses) // 2):
#         bracket = parentheses.popleft()
#         if bracket in ")}]":
#             is_unbalanced = True
#             break
#
#         if bracket == "{":
#             second_bracket = parentheses.pop()
#             if second_bracket == "}":
#                 continue
#             else:
#                 is_unbalanced = True
#                 break
#
#         elif bracket == "[":
#             second_bracket = parentheses.pop()
#             if second_bracket == "]":
#                 continue
#             else:
#                 is_unbalanced = True
#                 break
#         elif bracket == "(":
#             second_bracket = parentheses.pop()
#             if second_bracket == ")":
#                 continue
#             else:
#                 is_unbalanced = True
#                 break
#
#     if is_unbalanced:
#         return "NO"
#     else:
#         return "YES"
#
#
# def call_functions():
#     result = check_balance()
#     print(result)
#
#
# if __name__ == "__main__":
#     call_functions()


# --- #

# from collections import deque
#
#
# def get_deque():
#     brackets = deque(input())
#     return brackets
#
#
# def check_balance():
#     parentheses = get_deque()
#     spins = 0
#     is_unbalanced = False
#
#     while len(parentheses) > 0:
#
#         if spins >= len(parentheses):
#             is_unbalanced = True
#             break
#
#         if parentheses[0] == "(":
#             if parentheses[1] == ")":
#                 spins = 0
#                 parentheses.popleft()
#                 parentheses.popleft()
#         elif parentheses[0] == "[":
#             if parentheses[1] == "]":
#                 spins = 0
#                 parentheses.popleft()
#                 parentheses.popleft()
#         elif parentheses[0] == "{":
#             if parentheses[1] == "}":
#                 spins = 0
#                 parentheses.popleft()
#                 parentheses.popleft()
#
#         parentheses.rotate(-1)
#         spins += 1
#
#     if is_unbalanced:
#         return "NO"
#     else:
#         return "YES"
#
#
# def call_functions():
#     result = check_balance()
#     print(result)
#
# if __name__ == "__main__":
#     call_functions()


# -- Atanas Atanasov's solution

from collections import deque

expression = deque(input())

opening_brackets = "([{"
closing_brackets = ")]}"
counter = 0


while expression and counter < len(expression) / 2:
    if expression[0] not in opening_brackets:
        break
    index = opening_brackets.index(expression[0])
    if expression[1] == closing_brackets[index]:
        expression.popleft()
        expression.popleft()
        expression.rotate(counter)
        counter = 0
    else:
        expression.rotate(-1)
        counter += 1

if expression:
    print("NO")
else:
    print("YES")
