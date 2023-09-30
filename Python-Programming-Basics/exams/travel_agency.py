# Travel Agency

# Име на града - текст с възможности ("Bansko",  "Borovets", "Varna" или "Burgas")
# Вид на пакета - текст с възможности ("noEquipment",  "withEquipment", "noBreakfast" или "withBreakfast")
# Притежание на VIP отстъпка - текст с възможности  "yes" или "no"
# Дни за престой - цяло число в интервала [-10000 … 10000]

town = input()
package_type = input()
vip_discount = input()
days_stay = int(input())

if days_stay > 7:
    days_stay -= 1

bill_amount = 0

if days_stay < 1:
    print("Days must be positive number!")

elif town not in ["Bansko",  "Borovets", "Varna", "Burgas"]:
    print("Invalid input!")
elif package_type not in ["noEquipment",  "withEquipment", "noBreakfast", "withBreakfast"]:
    print("Invalid input!")

elif town == "Bansko" or town == "Borovets":
    if package_type == "withEquipment":
        if vip_discount == "yes":
            bill_amount = (days_stay * 100) * 0.90
        else:
            bill_amount = days_stay * 100
    else:
        if vip_discount == "yes":
            bill_amount = (days_stay * 80) * 0.95
        else:
            bill_amount = days_stay * 80

else:
    if package_type == "withBreakfast":
        if vip_discount == "yes":
            bill_amount = (days_stay * 130) * 0.88
        else:
            bill_amount = days_stay * 130
    else:
        if vip_discount == "yes":
            bill_amount = (days_stay * 100) * 0.93
        else:
            bill_amount = days_stay * 100

if bill_amount > 0:
    print(f"The price is {bill_amount :.2f}lv! Have a nice time!")
