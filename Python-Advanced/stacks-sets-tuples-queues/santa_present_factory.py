# Santa's Present Factory
# from collections import deque
#
#
# def is_it_christmas(unique_toys_crafted: set):
#     if "Teddy bear" in unique_toys_crafted and "Bicycle" in unique_toys_crafted \
#             or "Doll" in unique_toys_crafted and "Wooden train" in unique_toys_crafted:
#         print("The presents are crafted! Merry Christmas!")
#     else:
#         print("No presents this Christmas!")
#
#
# def materials_or_magic_left(materials: deque, magic_levels: deque):
#     if len(materials) > 0:
#         print(f"Materials left: {', '.join([str(materials.pop()) for _ in range(len(materials))])}")
#     elif len(magic_levels) > 0:
#         print(f"Magic left: {', '.join([str(magic_levels.popleft()) for _ in range(len(magic_levels))])}")
#
#
# def display_toys_crafted(unique_toys_crafted: set, toys_crafted: list):
#     unique_toys = sorted(list(unique_toys_crafted))
#     for toy in unique_toys:
#         print(f"{toy}: {toys_crafted.count(toy)}")
#
#
# def call_functions():
#     materials = deque([int(x) for x in input().split()])
#     magic_levels = deque([int(x) for x in input().split()])
#
#     toys = {
#         150: "Doll",
#         250: "Wooden train",
#         300: "Teddy bear",
#         400: "Bicycle"
#     }
#
#     toys_crafted = []
#     unique_toys_crafted = set()
#
#     # while len(materials) > 0 and len(magic_levels) > 0:
#     while materials and magic_levels:  # When the deque is empty it's False as well.
#         current_material = materials.pop()
#         current_magic_level = magic_levels.popleft()
#         magic_level = current_material * current_magic_level
#         if magic_level in toys:
#             toys_crafted.append(toys[magic_level])
#             unique_toys_crafted.add(toys[magic_level])
#         elif magic_level < 0:
#             values_sum = sum([current_material, current_magic_level])
#             materials.append(values_sum)
#         elif current_material == 0 and current_magic_level == 0:
#             continue
#         elif current_material == 0:
#             magic_levels.appendleft(current_magic_level)
#         elif current_magic_level == 0:
#             materials.append(current_material)
#         else:
#             materials.append(current_material + 15)
#
#     is_it_christmas(unique_toys_crafted)
#     materials_or_magic_left(materials, magic_levels)
#     display_toys_crafted(unique_toys_crafted, toys_crafted)
#
#
# if __name__ == "__main__":
#     call_functions()


# Atanas Atanasov's solution

from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

points = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
presents = {}

while materials and magic:
    total_magic = materials[-1] * magic[0]
    if total_magic in points:
        new_present = points[total_magic]
        if new_present not in presents:
            presents[new_present] = 0
        presents[new_present] += 1
        materials.pop()
        magic.popleft()
    elif total_magic < 0:
        materials.append(materials.pop() + magic.popleft())
    elif total_magic > 0:
        magic.popleft()
        materials[-1] += 15
    elif materials[-1] == 0 and magic[0] == 0:
        materials.pop()
        magic.popleft()
    elif materials[-1] == 0:
        materials.pop()
    elif magic[0] == 0:
        magic.popleft()
if ('Doll' in presents and "Wooden train" in presents) or ('Teddy bear' in presents and 'Bicycle' in presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")

if magic:
    print(f'Magic left: {", ".join([str(x) for x in magic])}')

for key, value in sorted(presents.items()):
    print(f"{key}: {value}")
