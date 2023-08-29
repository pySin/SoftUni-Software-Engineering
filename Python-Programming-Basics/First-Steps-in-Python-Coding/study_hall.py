# Study Hall

w = float(input())
h = float(input())

WORK_SPACE_W = 1.2
WORK_SPACE_H = 0.7
CORRIDOR_WIDTH = 1
AMENITIES_WORK_SPACES_LOSS = 3


width_rows_fit = (h - CORRIDOR_WIDTH) // WORK_SPACE_H
length_rows_fit = (w // WORK_SPACE_W)

# Fit work spaces formula
work_spaces_fit = (width_rows_fit * length_rows_fit) - AMENITIES_WORK_SPACES_LOSS
print(int(work_spaces_fit))
