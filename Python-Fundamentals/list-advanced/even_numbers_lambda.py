# Even Numbers with Lambda


number_list = list(map(int, input().split(", ")))

found_indices = map(lambda x: x if number_list[x] % 2 == 0 else "no", range(len(number_list)))
even_indices = list(filter(lambda a: a != "no", found_indices))
print(even_indices)
