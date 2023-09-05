# Swimming Pool Pipes

# Първият ред съдържа числото V – Обем на басейна в литри – цяло число в интервала [1…10000].
# Вторият ред съдържа числото P1 – дебит на първата тръба за час – цяло число в интервала [1…5000].
# Третият ред съдържа числото P2 – дебит на втората тръба за час– цяло число в интервала [1…5000].
# Четвъртият ред съдържа числото H – часовете които работникът отсъства – реално число в интервала [1.0…24.00]

pool_volume = int(input())
pipe_1_liters_hour = int(input())
pipe_2_liters_hour = int(input())
hours = float(input())

litters_from_pipe_1 = pipe_1_liters_hour * hours
litters_from_pipe_2 = pipe_2_liters_hour * hours
first_pipe_ratio = (litters_from_pipe_1 / (litters_from_pipe_1 + litters_from_pipe_2)) * 100
second_pipe_ratio = (litters_from_pipe_2 / (litters_from_pipe_1 + litters_from_pipe_2)) * 100

litters_filled = litters_from_pipe_1 + litters_from_pipe_2
pool_filled_percent = (litters_filled / pool_volume) * 100


if pool_volume >= litters_filled:
    print(f"The pool is {pool_filled_percent :.2f}% full. "
          f"Pipe 1: {first_pipe_ratio :.2f}%. Pipe 2: {second_pipe_ratio :.2f}%.")
else:
    print(f"For {hours :.2f} hours the pool "
          f"overflows with {litters_filled - pool_volume :.2f} liters.")
