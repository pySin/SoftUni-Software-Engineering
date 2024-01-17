# Address finder

import re


# 123 Redding Dr. 1560 Knoxville Ave. 3030 Norwalk Dr. 5 South St.
def find_addresses(addresses: str) -> list:
    pattern = r"(((?<=^)|(?<=\s))(\d+)\s(.+?)\.)"
    result = re.findall(pattern, addresses)
    return result


def save_addresses(addresses: list) -> dict:
    addresses_data = {address[-2]: address[-1] for address in addresses}
    return addresses_data


def call_functions():
    addresses_to_sift = input()
    addresses = find_addresses(addresses_to_sift)
    addresses_data = save_addresses(addresses)
    print(addresses_data)


if __name__ == "__main__":
    call_functions()
