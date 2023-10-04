#  Enough Milk To Sell
import time

USD_PER_LITER = 1.36

milk_finish = ""
seconds = 0
is_sell_possible = False
while milk_finish == "":
    time.sleep(1)
    seconds += 1

    if seconds > 19:
        is_sell_possible = True

    if seconds % 10 == 0:
        milk_finish = input("Press enter to continue or insert Yes to stop the milk flow: ")

if is_sell_possible:
    print(f"You will be payed {seconds * USD_PER_LITER :.2f}$ for {seconds} liters of milk")
else:
    print("Not enough milk to make a sell!")

