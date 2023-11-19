# Tribonacci Sequence


def tribonacci_sequence(length):

    sequence = []

    for i in range(1, length + 1):
        if i == 1:
            sequence.append(i)
        elif i <= 3:
            sequence.append(sum(sequence))
        else:
            sequence.append(sum(sequence[i - 4: i - 1]))
    return sequence


def call_functions():
    numbers_count = int(input())
    sequence = tribonacci_sequence(numbers_count)
    return " ".join([str(x) for x in sequence])


if __name__ == "__main__":
    sequence_result = call_functions()
    print(sequence_result)
