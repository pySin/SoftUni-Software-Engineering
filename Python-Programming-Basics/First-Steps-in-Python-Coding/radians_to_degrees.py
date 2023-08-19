# 2. Конвертор: от радиани в градуси
# градус = радиан * 180 / π. Числото π в Python може да достъпите чрез модула math.
# from math import pi
# from math import pi as referred_pi
#
# radians = float(input())
# degrees = radians * 180 / referred_pi
# print(degrees)

# 3. Калкулатор депозити
# сума = депозирана сума + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

# 1. Депозирана сума – реално число в интервала [100.00 … 10000.00]
# 2. Срок на депозита (в месеци) – цяло число в интервала [1…12]
# 3. Годишен лихвен процент – реално число в интервала [0.00 …100.00]

base_sum = int(input())
months = int(input())
interest_rate = float(input())

# Transform the yearly rate to monthly
monthly_interest_rate = interest_rate / 12
# Transform the percentages to multiplication value
multiplication_per_month = monthly_interest_rate / 100

monthly_increase = float(base_sum) * multiplication_per_month
final_sum = base_sum + (months * monthly_increase)

print(final_sum)
