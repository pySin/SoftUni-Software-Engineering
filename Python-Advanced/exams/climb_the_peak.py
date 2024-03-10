# Climb the peak
from collections import deque


food = [int(f) for f in input().split(", ")]
stamina = deque([int(s) for s in input().split(", ")])
peaks = deque([("Vihren", 80), ("Kutelo", 90), ("Banski Suhodol", 100), ("Polezhan", 60), ("Kamenitza", 70)])
peaks_conquered = []

for _ in range(7):
    current_food = food.pop()
    current_stamina = stamina.popleft()
    current_sum = current_food + current_stamina

    if current_sum >= peaks[0][1]:
        peaks_conquered.append(peaks.popleft())
        if not peaks:
            break

if not peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if peaks_conquered:
    peaks_display = "Conquered peaks:\n" + '\n'.join([f"{peak_[0]}" for peak_ in peaks_conquered])
    print(peaks_display)




