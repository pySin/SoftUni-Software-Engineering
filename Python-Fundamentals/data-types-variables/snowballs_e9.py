# Snowballs

# On the first input line, you will receive N – the number of snowballs.
# • On the next N*3 input lines, you will be receiving data about each snowball.
# The weight of the snowball (integer).
# • The time needed for the snowball to get to its target (integer).
# • The quality of the snowball (integer).

number_of_snowballs = int(input())

top_snowball_value = 0
top_snowball_weight = 0
top_snowball_time = 0
top_snowball_quality = 0

for snowball in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time_to_target = int(input())
    snowball_quality = int(input())

    snowball_value = round((snowball_weight / snowball_time_to_target) ** snowball_quality)
    if snowball_value > top_snowball_value:
        top_snowball_value = snowball_value
        top_snowball_weight = snowball_weight
        top_snowball_time = snowball_time_to_target
        top_snowball_quality = snowball_quality

print(f"{top_snowball_weight} : {top_snowball_time} = {top_snowball_value} ({top_snowball_quality})")
