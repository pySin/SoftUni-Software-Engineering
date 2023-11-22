# ASCII Values


def ascii_value(symbol):
    return ord(symbol)


def order_values(items):
    symbols = items.split(", ")
    symbol_value = {char: ord(char) for char in symbols}
    return symbol_value


if __name__ == "__main__":
    symbols_row = input()
    ordered_data = order_values(symbols_row)
    print(ordered_data)
