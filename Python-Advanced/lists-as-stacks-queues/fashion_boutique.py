# Fashion Boutique


clothes_box = [int(x) for x in input().split()]

rack_capacity = int(input())
number_of_racks = 1
current_rack = 0

while clothes_box:

    if current_rack + clothes_box[-1] >= rack_capacity:
        number_of_racks += 1
        current_rack = 0

    current_rack += clothes_box.pop()

print(number_of_racks)
