# Agency Profit

# Име на авиокомпанията - текст
# Брой билети за	 възрастни – цяло число в диапазона [1…400]
# Брой детски билети – цяло число в диапазона [25…120]
# Нетна цена на билет за възрастен – реално число в диапазона [100.0…1600.0]
# Цената на такса обслужване - реално число в диапазона [10.0…50.0]

flight_ticket_agency = input()
adults_tickets_count = int(input())
children_tickets_count = int(input())
adult_ticket_price = float(input())
administration_tax = float(input())

adult_tickets_sum = adults_tickets_count * (adult_ticket_price + administration_tax)
children_ticket_sum = children_tickets_count * ((adult_ticket_price * 0.30) + administration_tax)

final_income = adult_tickets_sum + children_ticket_sum
profit = final_income * 0.20

print(f"The profit of your agency from {flight_ticket_agency} tickets is {profit:.2f} lv.")
