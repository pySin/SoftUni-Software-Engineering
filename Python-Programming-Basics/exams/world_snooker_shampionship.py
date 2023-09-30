# World Snooker Championship


# Етап на първенството – текст - “Quarter final ”, “Semi final” или “Final”
# Вид на билета – текст - “Standard”, “Premium” или “VIP”
# Брой билети – цяло число в интервала [1 … 30]
# Снимка с трофея – символ – 'Y' (да) или 'N' (не)

competition_stage = input()  # “Quarter final ”, “Semi final” или “Final”
type_of_ticket = input()  # “Standard”, “Premium” или “VIP”
number_of_tickets = int(input())
picture_with_price = input()  # Y or N

price = 0

if competition_stage == "Quarter final":
    if type_of_ticket == "Standard":
        price = number_of_tickets * 55.50
    if type_of_ticket == "Premium":
        price = number_of_tickets * 105.20
    if type_of_ticket == "VIP":
        price = number_of_tickets * 118.90

if competition_stage == "Semi final":
    if type_of_ticket == "Standard":
        price = number_of_tickets * 75.88
    if type_of_ticket == "Premium":
        price = number_of_tickets * 125.22
    if type_of_ticket == "VIP":
        price = number_of_tickets * 300.40

if competition_stage == "Final":
    if type_of_ticket == "Standard":
        price = number_of_tickets * 110.810
    if type_of_ticket == "Premium":
        price = number_of_tickets * 160.66
    if type_of_ticket == "VIP":
        price = number_of_tickets * 400

# print(price)


if price > 4000:
    price *= 0.75
    if picture_with_price == "Y":
        pass
elif price > 2500:
    price *= 0.90
    if picture_with_price == "Y":
        price += number_of_tickets * 40
else:
    if picture_with_price == "Y":
        price += number_of_tickets * 40

print(f"{price :.2f}")
