# Cheese Showcase


def sorting_cheeses(**kwargs):
    sorted_dict = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    # sorted_dict = sorted(kwargs.items(), key=lambda kvp: (len(kvp[0]), len(kvp[1])))  # The length
    # of the name first, and the number of the pieces second.
    result = ""

    for name, quantities in sorted_dict:
        result += name + "\n"
        quantities = sorted(quantities, reverse=True)
        for num in quantities:
            result += str(num) + "\n"
    return result[:-1]


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camember=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
