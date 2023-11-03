# Sort Datatypes

def type_tell(item):
    if type(item) == int:
        return item, int
    elif type(item) == str:
        return item, str
    elif type(item) == float:
        return item, float
    elif type(item) == bool:
        return item, bool
    elif type(item) == list:
        return item, list
    elif type(item) == dict:
        return item, dict
    elif type(item) == tuple:
        return item, tuple


mixed_items = [4, "hello", 4.57, ["thrill", 2.45], (6, 9), False, {"key_1": 14}, 7, "Beech", (1, "Beer")]
get_datatypes = list(map(type_tell, mixed_items))


def type_sort(all_datatypes):
    integers = [int_item[0] for int_item in all_datatypes if "int" in str(int_item[1])]
    strings = [str_item[0] for str_item in all_datatypes if "str" in str(str_item[1])]
    floats = [float_item[0] for float_item in all_datatypes if "float" in str(float_item[1])]
    booleans = [tuple_item[0] for tuple_item in all_datatypes if "tuple" in str(tuple_item[1])]
    lists = [list_item[0] for list_item in all_datatypes if "list" in str(list_item[1])]
    dictionaries = [dict_item[0] for dict_item in all_datatypes if "dict" in str(dict_item[1])]
    return integers, strings, floats, booleans, lists, dictionaries


all_types = type_sort(get_datatypes)
print(all_types)
