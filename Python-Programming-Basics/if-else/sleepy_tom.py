# Sleepy Tom cat

GAME_MINUTES_PER_YEAR = 30000
GAME_MINUTES_PER_WORKING_DAY = 63
GAME_MINUTES_PER_DAY_OFF = 127

owner_holidays = int(input())

working_days = 365 - owner_holidays
time_for_play = (working_days * GAME_MINUTES_PER_WORKING_DAY) + (owner_holidays * GAME_MINUTES_PER_DAY_OFF)
time_available = GAME_MINUTES_PER_YEAR - time_for_play


if time_available < 0:
    H = abs(time_available) // 60
    M = abs(time_available) % 60
    print("Tom will run away")
    print(f"{H} hours and {M} minutes more for play")
else:
    H = (abs(time_available) // 60)
    M = abs(time_available % 60)
    print("Tom sleeps well")
    print(f"{H} hours and {M} minutes less for play")
