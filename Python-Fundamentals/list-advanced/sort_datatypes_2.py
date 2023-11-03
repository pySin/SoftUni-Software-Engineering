# Sort Datatypes 2

integers = []
strings = []
floats = []
booleans = []
lists = []
dictionaries = []
tuples = []


def type_sort(item):
    if type(item) == int:
        integers.append(item)
    elif type(item) == str:
        strings.append(item)
    elif type(item) == float:
        floats.append(item)
    elif type(item) == bool:
        booleans.append(item)
    elif type(item) == list:
        lists.append(item)
    elif type(item) == dict:
        dictionaries.append(item)
    elif type(item) == tuple:
        tuples.append(item)
    return type(item)


if __name__ == "__main__":
    mixed_items = [4, "hello", 4.57, ["thrill", 2.45], (6, 9), False, {"key_1": 14}, 7, "Beech", (1, "Beer")]
    single_datatype_lists = list(map(type_sort, mixed_items))

    print(single_datatype_lists)
    print(f"Integers: {integers}")
    print(f"Strings: {strings}")
    print(f"Floats: {floats}")
    print(f"Booleans: {booleans}")
    print(f"Dictionaries: {dictionaries}")
    print(f"Tuples: {tuples}")
