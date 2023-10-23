# Gladiator Expenses

# • On the first line, you will receive the lost fights count – an integer in the range [0, 1000].
# • On the second line, you will receive the helmet price - a floating-point number in the range [0, 1000].
# • On the third line, you will receive the sword price - a floating-point number in the range [0, 1000].
# • On the fourth line, you will receive the shield price - a floating-point number in the range [0, 1000].
# • On the fifth line, you will receive the armor price - a floating-point number in the range [0, 1000]

lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
shield_broken = 0

for fight in range(1, lost_fights_count + 1):
    if fight % 2 == 0:
        expenses += helmet_price

    if fight % 3 == 0:
        expenses += sword_price

    if fight % 2 == 0 and fight % 3 == 0:
        expenses += shield_price
        shield_broken += 1
        if shield_broken % 2 == 0:
            expenses += armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
