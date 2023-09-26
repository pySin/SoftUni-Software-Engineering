# Cat Walking

# На първия ред - минути разходка на ден - цяло число в интервала [1...50]
# На втория ред - броят на разходките дневно - цяло число в интервала [1…10]
# На третия ред - приетите от котката калории на ден – цяло число в интервала [100…4000]

minutes_walk = int(input())
walks_count = int(input())
calories_got = int(input())

calories_burnt = (minutes_walk * walks_count) * 5

if calories_burnt >= calories_got / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burnt}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burnt}.")
