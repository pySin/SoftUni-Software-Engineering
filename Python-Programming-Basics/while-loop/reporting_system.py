# Reporting System

# Сумата, която се очаква да бъде събрана от продажбите - цяло число в интервала [1 ... 10000]
# На всеки следващ ред, до получаване на командата "End" или докато не се съберат нужните средства:
# цените на предметите, които ще бъдат закупени - цяло число в интервала [1 ... 500]

target_amount = int(input())
money_collected = 0
payment_attempts = 0

cash_collected = 0
cash_collected_count = 0
card_collected = 0
card_collected_count = 0

command = input()
enough_money = False
while command != "End":
    payment_attempts += 1
    product_price = int(command)

    if payment_attempts % 2 != 0:
        if product_price > 100:
            print("Error in transaction!")
            # continue
        else:
            print("Product sold!")
            money_collected += product_price
            cash_collected += product_price
            cash_collected_count += 1
    else:
        if product_price < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            money_collected += product_price
            card_collected += product_price
            card_collected_count += 1

    if money_collected >= target_amount:
        enough_money = True
        break

    command = input()

if enough_money:
    print(f"Average CS: {cash_collected / cash_collected_count:.2f}")
    print(f"Average CC: {card_collected / card_collected_count:.2f}")
else:
    print(f"Failed to collect required money for charity.")
