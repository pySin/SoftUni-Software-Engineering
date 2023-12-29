# Ad Astra
import re


def find_food_items(food_info):
    pattern = r"([|#])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1"
    food_items = re.findall(pattern, food_info)
    return food_items


def display_data(food_items):

    all_calories = sum([(int(calories[3])) for calories in food_items])
    days = all_calories // 2000
    print(f"You have food to last you for: {days} days!")

    for food_item in food_items:
        name = food_item[1]
        date = food_item[2]
        calories = food_item[3]
        print(f"Item: {name}, Best before: {date}, Nutrition: {calories}")


def call_functions():
    food_info = input()
    food_items = find_food_items(food_info)
    display_data(food_items)


if __name__ == "__main__":
    call_functions()
