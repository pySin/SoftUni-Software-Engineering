# Mobile Operator

# Срок на договор – текст – "one", или "two"
# Тип на договор – текст – "Small",  "Middle", "Large"или "ExtraLarge"
# Добавен мобилен интернет – текст – "yes" или "no"
# Брой месеци за плащане - цяло число в интервала [1 … 24]

contract_length = input()
contract_type = input()
mobile_internet = input()
months = int(input())


final_sum = 0
if contract_length == "one":
    if contract_type == "Small":
        if mobile_internet == "yes":
            final_sum = months * (9.98 + 5.50)
        else:
            final_sum = months * 9.98
    if contract_type == "Middle":
        if mobile_internet == "yes":
            final_sum = months * (18.99 + 4.35)
        else:
            final_sum = months * 18.99
    if contract_type == "Large":
        if mobile_internet == "yes":
            final_sum = months * (25.98 + 4.35)
        else:
            final_sum = months * 25.98
    if contract_type == "ExtraLarge":
        if mobile_internet == "yes":
            final_sum = months * (35.99 + 3.85)
        else:
            final_sum = months * 35.99

if contract_length == "two":
    if contract_type == "Small":
        if mobile_internet == "yes":
            final_sum = (months * (8.58 + 5.50)) * (1 - 0.0375)
        else:
            final_sum = (months * 8.58) * (1 - 0.0375)
    if contract_type == "Middle":
        if mobile_internet == "yes":
            final_sum = (months * (17.09 + 4.35)) * (1 - 0.0375)
        else:
            final_sum = (months * 17.09) * (1 - 0.0375)
    if contract_type == "Large":
        if mobile_internet == "yes":
            final_sum = (months * (23.59 + 4.35)) * (1 - 0.0375)
        else:
            final_sum = (months * 23.59) * (1 - 0.0375)
    if contract_type == "ExtraLarge":
        if mobile_internet == "yes":
            final_sum = (months * (31.79 + 3.85)) * (1 - 0.0375)
        else:
            final_sum = (months * 31.79) * (1 - 0.0375)

print(f"{final_sum :.2f} lv.")
