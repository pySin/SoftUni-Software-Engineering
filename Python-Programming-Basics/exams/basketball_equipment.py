# Basketball Equipment

# Годишната такса за тренировки по баскетбол – цяло число в интервала [0… 9999]

yearly_fee = int(input())

trainers = yearly_fee * 0.60
training_suit = trainers * 0.80
ball = training_suit / 4
accessories = ball / 5

whole_purchase = yearly_fee + trainers + training_suit + ball + accessories

print(f"{whole_purchase :.2f}")
