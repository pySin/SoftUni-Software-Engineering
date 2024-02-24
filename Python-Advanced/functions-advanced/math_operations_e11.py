# Math Operations 2
# from collections import deque
#
#
# def math_operations(*args, **kwargs):
#     from collections import deque
#
#     math_ops = {
#         "a": lambda x: kwargs["a"] + x,
#         "s": lambda x: kwargs["s"] - x,
#         "d": lambda x: kwargs["d"] / x if x != 0 else kwargs["d"],
#         "m": lambda x: kwargs["m"] * x if x != 0 else kwargs["m"]
#     }
#
#     operations = deque(["a", "s", "d", "m"])
#
#     for f_number in args:
#         operation = operations[0]
#         operations.rotate(-1)
#         kwargs[operation] = math_ops[operation](f_number)
#     sorted_results = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], kvp[0]))
#     return "\n".join([f"{x[0]}: {x[1]:.1f}" for x in sorted_results])
#
#
# print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
# print()
# print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
# print()
# print(math_operations(6.0, a=0, s=0, d=5, m=0))

# -- Atanas Atanasov's solution


def math_operations(*args, **kwargs):
    for i in range(len(args)):  # Use modular division to loop from 1 to 4
        if i % 4 == 0:
            kwargs["a"] += args[i]
        elif i % 4 == 1:
            kwargs["s"] -= args[i]
        elif i % 4 == 2:
            if not args[i] == 0:
                kwargs["d"] /= args[i]
        else:
            kwargs["m"] *= args[i]
    result = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    return "\n".join([f"{key}: {value:.1f}" for key, value in result])


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print()
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print()
print(math_operations(6.0, a=0, s=0, d=5, m=0))
