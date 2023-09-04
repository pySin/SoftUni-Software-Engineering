# Shopping

# ⦁	Бюджетът на Петър - реално число в интервала [1.0…100000.0]
# ⦁	Броят видеокарти - цяло число в интервала [1…100]
# ⦁	Броят процесори - цяло число в интервала [1…100]
# ⦁	Броят рам памет - цяло число в интервала [1…100]

VIDEO_CARD = 250

budget = float(input())
video_card_count = int(input())
processors_count = int(input())
ram_memory_count = int(input())

video_cards_sum = video_card_count * VIDEO_CARD
processor_sum = (processors_count * (video_cards_sum * 0.35))
ram_memory_sum = (ram_memory_count * (video_cards_sum * 0.10))

full_sum = video_cards_sum + processor_sum + ram_memory_sum

if video_card_count > processors_count:
    full_sum *= (1 - 0.15)

if full_sum <= budget:
    print(f"You have {budget - full_sum :.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(budget - full_sum) :.2f} leva more!")
