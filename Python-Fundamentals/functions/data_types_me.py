# Data Types


def data_manage(data_1, data_2):
    if data_1 == "int":
        return int(data_2) * 2
    elif data_1 == "real":
        return f"{float(data_2) * 1.5 :.2f}"
    elif data_1 == "string":
        return "$" + data_2 + "$"


if __name__ == "__main__":
    data_type = input()
    data_x = input()
    result = data_manage(data_type, data_x)
    print(result)
