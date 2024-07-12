# Ski Trip

# ⦁	Първи ред - дни за престой - цяло число в интервала [0...365]
# ⦁	Втори ред - вид помещение - "room for one person", "apartment" или "president apartment"
# ⦁	Трети ред - оценка - "positive"  или "negative"

days = int(input())
type_of_accommodation = input()  # "room for one person", "apartment" или "president apartment"
evaluation = input()  # "positive"  или "negative"
days -= 1

accommodation_price = 0

if type_of_accommodation == "room for one person":
    accommodation_price = days * 18

if type_of_accommodation == "apartment":
    accommodation_price = days * 25
    print(accommodation_price)
    if days < 10:
        accommodation_price *= 0.70
    elif 10 <= days <= 15:
        accommodation_price *= 0.65
    elif days > 15:
        accommodation_price *= 0.50
    print(accommodation_price)
if type_of_accommodation == "president apartment":
    accommodation_price = days * 35
    if days < 10:
        accommodation_price *= 0.90
    elif 10 <= days <= 15:
        accommodation_price *= 0.85
    elif days > 15:
        accommodation_price *= 0.80

if evaluation == "positive":
    accommodation_price *= 1.25
elif evaluation == "negative":
    accommodation_price *= 0.90

print(f"{accommodation_price :.2f}")
