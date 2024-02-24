# Negative VS Positive


def pos_neg(*args):
    positives = 0
    negatives = 0
    for number in args:
        if number < 0:
            negatives += number
        elif number > 0:
            positives += number
    return positives, negatives


def call_functions():
    numbers = [int(x) for x in input().split()]
    positives, negatives = pos_neg(*numbers)
    print(negatives)
    print(positives)
    if abs(negatives) > positives:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


if __name__ == "__main__":
    call_functions()
