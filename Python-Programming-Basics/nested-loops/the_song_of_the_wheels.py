# The Song Of The Wheels

# От конзолата се чете едно цяло число (контролната стойност): M – цяло число в интервала [4 … 144]
CODE_DIGIT_LIMIT = 9

control_number = int(input())
passwords = 0
is_forth_password = False
forth_password = ""

# if control_number > 9:
#     control_number = 10


for a in range(1, CODE_DIGIT_LIMIT + 1):
    for b in range(1, CODE_DIGIT_LIMIT + 1):
        for c in range(1, CODE_DIGIT_LIMIT + 1):
            for d in range(1, CODE_DIGIT_LIMIT + 1):
                if (a * b) + (c * d) == control_number and a < b and c > d:
                    passwords += 1
                    if passwords == 4:
                        forth_password = str(a) + str(b) + str(c) + str(d)
                        #  if len(forth_password) < 5:
                        is_forth_password = True

                    if len(f"{a}{b}{c}{d}") < 5:
                        print(f"{a}{b}{c}{d}", end=" ")

if is_forth_password:
    print()
    print(f"Password: {forth_password}")
else:
    print()
    print("No!")
