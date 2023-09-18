# Vacation

# ⦁	Пари, нужни за екскурзията - реално число;
# ⦁	Налични пари - реално число.
# След това многократно се четат по два реда:
# ⦁	Вид действие – текст с две възможности: "spend" или "save";
# ⦁	Сумата, която ще спести/похарчи - реално число.

vacation_money = float(input())
money_available = float(input())

spending_days_in_a_row = 0
days_passed = 0

is_five_spending = False
while money_available < vacation_money:
    days_passed += 1
    spend_or_save = input()
    current_money = float(input())

    if spend_or_save == "spend":
        if current_money >= money_available:
            money_available = 0
        else:
            money_available -= current_money
        spending_days_in_a_row += 1
        if spending_days_in_a_row == 5:
            is_five_spending = True
            break
        continue
    spending_days_in_a_row = 0
    money_available += current_money

if is_five_spending:
    print(f"You can't save the money.")
    print(f"{days_passed}")
else:
    print(f"You saved the money for {days_passed} days.")
