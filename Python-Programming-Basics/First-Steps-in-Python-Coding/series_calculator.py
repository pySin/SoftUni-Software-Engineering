# Series calculator

# Име на сериал - текст
# Брой сезони – цяло число в диапазона [1… 10]
# Брой епизоди  – цяло число в диапазона [10… 80]
# Времетраене на обикновен епизод без рекламите – реално число в диапазона [40.0… 65.0]

tv_series_name = input()
number_of_seasons = int(input())
number_of_episodes = int(input())
episode_duration = float(input())

normal_duration_sum = number_of_seasons * number_of_episodes * episode_duration
duration_with_ads = normal_duration_sum + (normal_duration_sum * 0.20)
extra_episodes_added_duration = duration_with_ads + (number_of_seasons * 10)


print(f"Total time needed to watch the {tv_series_name} series \
is {int(extra_episodes_added_duration)} minutes.")
