# Energy Booster

# Плод - текст с възможности: "Watermelon", "Mango", "Pineapple" или "Raspberry"
# Размерът на сета - текст с възможности: "small" или "big"
# Брой на поръчаните сетове - цяло число в интервала [1 … 10000]

fruit_gel = input()  # "Watermelon", "Mango", "Pineapple" или "Raspberry"
set_size = input()  # "small" или "big"
sets_count = int(input())
amount_due = 0

if set_size == "small":
    if fruit_gel == "Watermelon":
        amount_due = (sets_count * 2) * 56
    if fruit_gel == "Mango":
        amount_due = (sets_count * 2) * 36.66
    if fruit_gel == "Pineapple":
        amount_due = (sets_count * 2) * 42.10
    if fruit_gel == "Raspberry":
        amount_due = (sets_count * 2) * 20
if set_size == "big":
    if fruit_gel == "Watermelon":
        amount_due = (sets_count * 5) * 28.70
    if fruit_gel == "Mango":
        amount_due = (sets_count * 5) * 19.60
    if fruit_gel == "Pineapple":
        amount_due = (sets_count * 5) * 24.80
    if fruit_gel == "Raspberry":
        amount_due = (sets_count * 5) * 15.20

if 400 <= amount_due <= 1000:
    amount_due *= 0.85
elif amount_due > 1000:
    amount_due *= 0.50

print(f"{amount_due :.2f} lv.")
