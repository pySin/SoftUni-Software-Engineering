# Let's sort this list

def asc_des_none(lst, s):
    if s == "Asc":
        lst.sort()
        return lst
    elif s == "Des":
        lst.sort(reverse=True)
        return lst
    elif s == "None":
        return lst


direction = input()  # Asc - Des - None
print(asc_des_none([1, 3, 2, 9, 6], direction))
