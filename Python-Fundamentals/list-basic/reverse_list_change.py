# Reverse list change

straight_list = [1, 2, 3, 4, 5, 6]

# print(len(straight_list))

for i in range(len(straight_list)-1, -1, -1):
    print(i)
    if straight_list[i] % 2 == 0:
        straight_list.remove(straight_list[i])

print(straight_list)
