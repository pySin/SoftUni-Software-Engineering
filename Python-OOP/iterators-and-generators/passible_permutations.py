# Possible Permutations

def possible_permutations(ls: list):
    if len(ls) <= 1:
        yield ls
    else:
        for i in range(len(ls)):
            for perm in possible_permutations(ls[:i] + ls[i + 1:]):
                yield [ls[i]] + perm

    # permutations = []

    # for n1 in base_numbers:
    #     for n2 in base_numbers:
    #         if n1 == n2:
    #             continue
    #         for n3 in base_numbers:
    #             if n2 == n3 or n1 == n3:
    #                 continue
    #             yield [n1, n2, n3]
    #             # if [n1, n2, n3] not in permutations:
                    # permutations.append([n1, n2, n3])
    # return permutations


[print(n) for n in possible_permutations([1, 2, 3])]
