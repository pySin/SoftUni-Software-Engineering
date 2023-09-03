# lunch break
from math import ceil

# ⦁	Име на сериал – текст
# ⦁	Продължителност на епизод  – цяло число в диапазона [10… 90]
# ⦁	Продължителност на почивката  – цяло число в диапазона [10… 120]

tv_series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
relax_time = break_duration / 4

time_for_episode = break_duration - (lunch_time + relax_time)

if episode_duration <= time_for_episode:
    print(f"You have enough time to watch {tv_series_name} and"
          f" left with {ceil(time_for_episode - episode_duration)} minutes free time.")
else:
    print(f"You don't have enough time to watch {tv_series_name}, "
          f"you need {ceil(abs(time_for_episode - episode_duration))} more minutes.")
