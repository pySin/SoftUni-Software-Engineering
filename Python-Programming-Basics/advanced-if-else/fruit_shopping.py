# Fruit Shopping

fruit_or_vegetable = input()
item = ""
if fruit_or_vegetable == "banana" \
        or fruit_or_vegetable == "apple" \
        or fruit_or_vegetable == "kiwi" \
        or fruit_or_vegetable == "cherry" \
        or fruit_or_vegetable == "lemon" \
        or fruit_or_vegetable == "grapes":
    item = "fruit"
elif fruit_or_vegetable == "tomato" \
        or fruit_or_vegetable == "cucumber" \
        or fruit_or_vegetable == "pepper" \
        or fruit_or_vegetable == "carrot":
    item = "vegetable"
else:
    item = "unknown"

print(item)
