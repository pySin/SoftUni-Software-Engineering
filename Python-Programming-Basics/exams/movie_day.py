# Movie day
TIME_TRAIN = 0.15

# Време за снимки – цяло число в диапазона [0… 1440]
# Брой сцени  – цяло число в диапазона [5… 25]
# Времетраене на сцена – цяло число в диапазона [20… 90]


time_available = int(input())
scenes_count = int(input())
scene_length = int(input())

time_for_shootings = scenes_count * scene_length
time_needed = time_for_shootings + (time_available * TIME_TRAIN)

if time_available >= time_needed:
    print(f"You managed to finish the movie on time! "
          f"You have {round(time_available - time_needed)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(time_needed - time_available)} minutes.")
