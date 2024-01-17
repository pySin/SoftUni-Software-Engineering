# Show all bottom level pairs from nested dictionaries
# with different depths


def nested_dict(pairs, target_dictionary):
    for key_1, value_1 in target_dictionary.items():
        if type(value_1) == dict:
            nested_dict(pairs, value_1)
        else:
            pairs.append(str(key_1) + " - " + str(value_1))
    return pairs


def single_pair(pairs, target_dictionary):
    for key, value in target_dictionary.items():
        if type(value) == dict:
            nested_dict(pairs, value)
        else:
            pairs.append(str(key) + " - " + str(value))
    return pairs


def function_call():
    pairs = []
    dictionary_1 = {
        "key_1": "value_1",
        "key_2": {
            "key_1": "value_1",
            "key_3": 3
        },
        "key_3": {
            "key_2": {
                "key_a": "value_a",
                "key_b": "value_b"
            },
            "key_3": {
                "key_1": "value_1",
                "key_2": "value_2"
            }
        }
    }

    return single_pair(pairs, dictionary_1)


if __name__ == "__main__":
    for pair in function_call():
        print(pair)
