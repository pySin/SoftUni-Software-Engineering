#
from math import floor

# ⦁	Рекордът в секунди – реално число;
# ⦁	Разстоянието в метри – реално число;
# ⦁	Времето в секунди, за което плува разстояние от 1 м. - реално число.

RESISTENCE_DELAY_PER_15_METERS = 12.5

swimming_record = float(input())
distance_meters = float(input())
seconds_per_meter = float(input())

no_water_resistance_time = distance_meters * seconds_per_meter
resistance = floor(distance_meters / 15) * RESISTENCE_DELAY_PER_15_METERS
swimming_time = no_water_resistance_time + resistance
ivancho_time = swimming_time - swimming_record

if ivancho_time < 0:
    print(f"Yes, he succeeded! The new world record is {swimming_time :.2f} seconds.")
else:
    print(f"No, he failed! He was {ivancho_time :.2f} seconds slower.")
