# Building Pie Chart

DEGREES_IN_A_CIRCLE = 360


def angle_amplitude(ratios):
    ratio_sum = sum(ratios.values())

    for key, value in ratios.items():
        ratios[key] = round(DEGREES_IN_A_CIRCLE * (value / ratio_sum), 2)

    return ratios


if __name__ == "__main__":
    target_ratios = {"a": 8, "b": 21, "c": 12, "d": 5, "e": 4}
    result_dict = angle_amplitude(target_ratios)
    print(result_dict)
