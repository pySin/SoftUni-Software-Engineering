# pop() deletes but also returns value

# my_list = [1, 4, 2, 7, "Hello", "Li"]
#
# stored_pop = my_list.pop(4)
# print(stored_pop)
# my_list.append(my_list.pop(0))  # pop an element and append it to the end of the list
# print(my_list)

my_list = [1, 4, 2, 7, "Hello", "Li"]

# for item in range(len(my_list)-1, -1, -1):
#     print(item)

my_list.reverse()
print(my_list)
