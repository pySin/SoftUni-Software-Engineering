# PC Store
USD_TO_BGN = 1.57

# •	На първи ред: цената в долари за процесора – реално число в интервала [200.00 … 3000.00]
# •	На втори ред: цената в долари за видео карта – реално число в интервала [100.00 … 1500.00]
# На трети ред: цената в долари за една RAM памет – реално число в интервала [80.00 ... 500.00]
# •	На четвърти: ред брой RAM памети – цяло число в интервала [1 ... 4]
# •   На пети ред: процент отстъпка – реално число в интервала [0.01 … 0.1]

processor_price_usd = float(input())
video_card_price_usd = float(input())
ram_price_usd = float(input())
ram_count = int(input())
discount_percent = float(input())

money_needed = ((processor_price_usd * USD_TO_BGN) *
                (1 - discount_percent)) + ((video_card_price_usd * USD_TO_BGN) * (1 - discount_percent)) \
               + ((ram_price_usd * USD_TO_BGN) * ram_count)


print(f"Money needed - {money_needed :.2f} leva.")
