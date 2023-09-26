# Computer Hall

# На първия ред - месецът - текст с възможности: "march", "april", "may", "june", "july", "august"
# На втория ред - броят на прекараните часове - цяло число в диапазона [1...10]
# На третия ред - броят на хората в групата -  цяло число в диапазона [1...10]
# На четвъртия ред - времето от деня – текст с възможности: "day" или "night"

month = input()
hours_of_service = int(input())
number_of_people = int(input())
time_of_the_day = input()

bill_per_person = 0

if month == "march" or month == "april" or month == "may":
    if time_of_the_day == "day":
        bill_per_person = hours_of_service * 10.50
    elif time_of_the_day == "night":
        bill_per_person = hours_of_service * 8.40
elif month == "june" or month == "july" or month == "august":
    if time_of_the_day == "day":
        bill_per_person = hours_of_service * 12.60
    elif time_of_the_day == "night":
        bill_per_person = hours_of_service * 10.20


if number_of_people >= 4:
    bill_per_person *= 0.90

if hours_of_service >= 5:
    bill_per_person *= 0.50

price_per_hour = round(bill_per_person / hours_of_service, 2)
print(f"Price per person for one hour: {price_per_hour:.2f}")
print(f"Total cost of the visit: {price_per_hour * hours_of_service * number_of_people:.2f}")
