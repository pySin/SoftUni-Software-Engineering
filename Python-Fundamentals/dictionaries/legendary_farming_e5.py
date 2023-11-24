# Legendary Farming


def farming():

    legendary_materials = {
         "shards": 0,
         "fragments": 0,
         "motes": 0
    }

    is_legendary = False

    while True:
        line_of_items = input().split()
        for i in range(0, len(line_of_items), 2):
            material = line_of_items[i + 1].lower()
            amount = int(line_of_items[i])

            if material in legendary_materials.keys():
                legendary_materials[material] += amount
            else:
                legendary_materials[material] = amount

            if legendary_materials["shards"] >= 250:
                print("Shadowmourne obtained!")
                legendary_materials["shards"] -= 250
                is_legendary = True
                break
            elif legendary_materials["fragments"] >= 250:
                print("Valanyr obtained!")
                legendary_materials["fragments"] -= 250
                is_legendary = True
                break
            elif legendary_materials["motes"] >= 250:
                print("Dragonwrath obtained!")
                legendary_materials["motes"] -= 250
                is_legendary = True
                break

        if is_legendary:
            break

    return legendary_materials


for materials, amounts in farming().items():
    print(f"{materials}: {amounts}")
