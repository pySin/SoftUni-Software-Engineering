# Matching Parentheses


# algebraic_expression = list(input())
# inner_brackets = []
#
# opening_brackets = 0
# brackets_to_close = 0
# locked_brackets = []
#
# for i in range(len(algebraic_expression)):
#     current_symbol = algebraic_expression.pop()
#     if current_symbol == ")":
#         opening_brackets += 1
#         brackets_to_close += 1
#         inner_brackets.append([])
#
#     if opening_brackets > 0:
#         for j in range(brackets_to_close):
#             if j not in locked_brackets:
#                 inner_brackets[j].append(current_symbol)
#
#     if current_symbol == "(":
#         locked_brackets.append(brackets_to_close - 1)
#         opening_brackets -= 1
#
#
# # print(inner_brackets)
# for i in range(len(inner_brackets) - 1, - 1, - 1):
#     math_operations = inner_brackets[i]
#     math_phrase = ""
#     for j in range(len(math_operations)):
#         math_phrase += math_operations.pop()
#     print(math_phrase)


# -- 2nd variety

algebraic_expression = list(input())

opening_bracket_index = []

for i in range(len(algebraic_expression)):
    if algebraic_expression[i] == "(":
        opening_bracket_index.append(i)

    if algebraic_expression[i] == ")":
        print("".join(algebraic_expression[opening_bracket_index.pop(): i + 1]))

