# Food Delivery

# Food Prices
CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEGETARIAN_MENU = 8.15

# Order
chicken_menus_count = int(input())
fish_menus_count = int(input())
vegetarian_menus_count = int(input())
delivery_charge = 2.50
dessert_bill_percentage = 20

no_dessert_bill = (CHICKEN_MENU * chicken_menus_count)\
    + (FISH_MENU * fish_menus_count)\
    + (VEGETARIAN_MENU * vegetarian_menus_count)

dessert_bill = (no_dessert_bill * (dessert_bill_percentage / 100))

full_bill = no_dessert_bill + dessert_bill + delivery_charge
print(full_bill)
