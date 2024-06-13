# Sort positives keep negatives

# pos_neg_sort([6, 3, -2, 5, -8, 2, -2]) ➞ [2, 3, -2, 5, -8, 6, -2]
# pos_neg_sort([6, 5, 4, -1, 3, 2, -1, 1]) ➞ [1, 2, 3, -1, 4, 5, -1, 6]
# pos_neg_sort([-5, -5, -5, -5, 7, -5]) ➞ [-5, -5, -5, -5, 7, -5]
# pos_neg_sort([]) ➞ []

nested_numbers = [[6, 3, -2, 5, -8, 2, -2], [6, 5, 4, -1, 3, 2, -1, 1], [-5, -5, -5, -5, 7, -5],
                  [-5, -5, -5, -5, -4, -5], [-5, 4, -8, 3, -1, 2, 1, -7], [-5, 4, 3]]


def pos_neg_sort(lst):
    positive_list = []
    for list_number in lst:
        if list_number >= 0:
            positive_list.append(list_number)
    positive_list.sort()
    # print(positive_list)

    positive_index = 0
    for i in range(len(lst)):
        if lst[i] >= 0:
            lst[i] = positive_list[positive_index]
            positive_index += 1

    print(lst)


for nested_list in nested_numbers:
    pos_neg_sort(nested_list)
