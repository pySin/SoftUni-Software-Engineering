# Largest of three numbers

# number_one = int(input())
# number_two = int(input())
# number_three = int(input())
#
# if number_three < number_one > number_two:
#     print(number_one)
# elif number_one < number_two > number_three:
#     print(number_two)
# else:
#     print(number_three)

number_1, number_2, number_3 = int(input()), int(input()), int(input())
print(max(number_1, number_2, number_3))
