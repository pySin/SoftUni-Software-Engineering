# Easter Bread

budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
one_liter_milk_price = flour_price * 1.25

breads_made = 0
colored_eggs = 0

milk_volume = 0
while True:

    # if milk_volume < 0.25:
    #     if budget < one_liter_milk_price + flour_price + eggs_price:
    #         break
    #     else:
    #         budget -= one_liter_milk_price + flour_price + eggs_price
    #         breads_made += 1
    #         colored_eggs += 3
    #         milk_volume += 1
    #         milk_volume -= 0.25
    if budget < flour_price + eggs_price + (one_liter_milk_price / 4):
        break
    else:
        budget -= flour_price + eggs_price + (one_liter_milk_price / 4)
        breads_made += 1
        colored_eggs += 3
        milk_volume -= 0.25

    if breads_made % 3 == 0:
        colored_eggs -= breads_made - 2

print(f"You made {breads_made} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget :.2f}BGN left.")
