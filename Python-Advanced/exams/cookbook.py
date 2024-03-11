# Cookbook


def cookbook(*args):
    cuisines = {}

    for recipe, cuisine, ingredients in args:
        if cuisine not in cuisines:
            cuisines[cuisine] = []
        cuisines[cuisine].append((recipe, ingredients))

    for current_cuisine, current_recipes in cuisines.items():
        cuisines[current_cuisine] = sorted(current_recipes)

    cuisines = sorted(cuisines.items(), key=lambda x: (-len(x[1]), x[0]))
    # print(cuisines)

    display_recipes = ""
    for cuisine_display in cuisines:
        display_recipes += f"{cuisine_display[0]} cuisine contains {len(cuisine_display[1])} recipes:\n"
        for recipe_display in cuisine_display[1]:
            current_ingredients = ", ".join(recipe_display[1])
            display_recipes += f"  * {recipe_display[0]} -> Ingredients: {current_ingredients}\n"

    return display_recipes[:-1]


# print(cookbook(
#     ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
#     ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
#     ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
#     ("Croissant", "French", ["flour", "butter", "yeast"]),
#     ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
# ))


# print(cookbook(
#     ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
#     ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
#     ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
#     ("Croissant", "French", ["flour", "butter", "yeast"]),
#     ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
#     ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
#     ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
#     ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
#     ))

print(cookbook(
    ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
    ))
