# Aluminium Joinery

# Брой дограми – цяло число в интервала [0..1000];
# Вид на дограмите – текст "90X130" или "100X150" или "130X180" или "200X300";
# Начин на получаване – текст
# С доставка - "With delivery"
# Без доставка - "Without delivery"

number_of_joinery = int(input())
type_of_joinery = input()  # "90X130" или "100X150" или "130X180" или "200X300"
delivery = input()  # With delivery, "Without delivery"

price = 0

is_order = False
if type_of_joinery == "90X130":
    if number_of_joinery < 10:
        is_order = True
    elif 30 < number_of_joinery <= 60:
        price = (number_of_joinery * 110) * 0.95
    elif number_of_joinery > 60:
        price = (number_of_joinery * 110) * 0.92
    else:
        price = (number_of_joinery * 110)
elif type_of_joinery == "100X150":
    if number_of_joinery < 10:
        is_order = True
    elif 40 < number_of_joinery <= 80:
        price = (number_of_joinery * 140) * 0.94
    elif number_of_joinery > 80:
        price = (number_of_joinery * 140) * 0.90
    else:
        price = (number_of_joinery * 140)
elif type_of_joinery == "130X180":
    if number_of_joinery < 10:
        is_order = True
    elif 20 < number_of_joinery <= 50:
        price = (number_of_joinery * 190) * 0.93
    elif number_of_joinery > 50:
        price = (number_of_joinery * 190) * 0.88
    else:
        price = (number_of_joinery * 190)
elif type_of_joinery == "200X300":
    if number_of_joinery < 10:
        is_order = True
    elif 25 < number_of_joinery <= 50:
        price = (number_of_joinery * 250) * 0.91
    elif number_of_joinery > 50:
        price = (number_of_joinery * 250) * 0.86
    else:
        price = (number_of_joinery * 250)
if delivery == "With delivery":
    price += 60

if number_of_joinery > 99:
    price *= 0.96

if is_order:
    print("Invalid order")
else:
    print(f"{price:.2f} BGN")
