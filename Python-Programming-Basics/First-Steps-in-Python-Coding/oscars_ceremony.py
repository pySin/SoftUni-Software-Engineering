# Oscar ceremony

hall_hire = int(input())

figurine = hall_hire * 0.7
catering = figurine * 0.85
sound = catering * 0.5

ceremony_bill = hall_hire + figurine + catering + sound
print(f"{ceremony_bill:.2f}")
