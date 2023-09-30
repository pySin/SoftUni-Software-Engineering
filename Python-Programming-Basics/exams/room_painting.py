# Room Painting
from math import ceil, floor


# Броя кутии с боя – цяло число в интервала [1 … 10 000]
# Броя на ролките тапети – цяло число в интервала [1 ... 10 000]
# Цената за един чифт ръкавици – реално число  в интервала [0.00 ... 1000.00]
# Цената за една четка – реално число  в интервала [0.00 ... 2000.00]

BOX_PAINT_PRICE = 21.50
WALLPAPER_PRICE = 5.20

boxes_of_paint = int(input())
wallpapers = int(input())
gloves_per_pair = float(input())
brush_price = float(input())

amount_due = (boxes_of_paint * BOX_PAINT_PRICE) + (WALLPAPER_PRICE * wallpapers) \
             + (ceil(wallpapers * 0.35) * gloves_per_pair) + \
             (floor(boxes_of_paint * 0.48) * brush_price)

print(f"This delivery will cost {(amount_due / 15):.2f} lv.")
