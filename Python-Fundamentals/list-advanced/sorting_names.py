# Sorting Names

def sort_name(name_list):
    nested_names = []
    for name in name_list:
        name_len = len(name)
        same_len_list = []
        for len_sort in name_list:
            if len(len_sort) == name_len:
                same_len_list.append(len_sort)
        if same_len_list not in nested_names:
            nested_names.append(same_len_list)
    nested_names.sort(key=lambda x: len(x[0]), reverse=True)
    nested_sorted_names = []
    for current_list in nested_names:
        current_list.sort()
        nested_sorted_names.extend(current_list)
    print(nested_sorted_names)


initial_names = input().split(", ")
# initial_names.sort(key=len, reverse=True)
sort_name(initial_names)

