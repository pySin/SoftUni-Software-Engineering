# Save Password Generators

# ⦁	На първия ред a – цяло число в интервала [1 … 1000]
# ⦁	На втория ред b – цяло число в интервала [1 … 1000]
# ⦁	На третия ред максимален брой генерирани пароли – цяло число в интервала [1 … 1000000]

a = int(input())
b = int(input())
max_passwords_count = int(input())
max_a_range = 56
max_b_range = 97
# print(chr(36))


step_a = 0
step_b = 0
count_combinations = 0
x = 0
y = 0
is_max_passwords = False
for i in range(35, 35 + a):
    x += 1
    for j in range(64, 64 + b):
        y += 1
        print(chr(35 + step_a) + chr(64 + step_b) + str(x)
              + str(y) + chr(64 + step_b) + chr(35 + step_a), end="|")
        count_combinations += 1
        step_a += 1
        step_b += 1

        if step_a == max_a_range - 35:
            step_a = 0

        if step_b == max_b_range - 64:
            step_b = 0

        if count_combinations == max_passwords_count:
            is_max_passwords = True
            break
    if is_max_passwords:
        break
    y = 0

# for i in range(35, 35 + a):
#     for j in range(64, 64 + b):
#         #  for x in range(1, a):
#             #  for y in range(1, b):
#         print(chr(35 + step), end="")
#         print(chr(64 + step), end="")
#         print(str(1), end="")
#         print(str(1), end="")
#         print(chr(35 + step), end="")
#         print(chr(64 + step), end="|")
#
#         step += 1
