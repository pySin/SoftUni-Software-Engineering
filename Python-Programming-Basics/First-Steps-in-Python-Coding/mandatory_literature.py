# Painting

# · Предпазен найлон - 1.50 лв. за кв. метър
# · Боя - 14.50 лв. за литър
# · Разредител за боя - 5.00 лв. за литър

cling_film_sq_m = 1.50
paint_per_liter = 14.50
thinner_per_litter = 5.00
bags = 0.40

# 1. Необходимо количество найлон (в кв.м.) - цяло число в интервала [1... 100]
# 2. Необходимо количество боя (в литри) - цяло число в интервала [1…100]
# 3. Количество разредител (в литри) - цяло число в интервала [1…30]
# 4. Часовете, за които майсторите ще свършат работата - цяло число в интервала [1…9]

cling_film = int(input())
cling_film = cling_film + 2
paint = int(input())
paint = paint + (paint * 0.10)
thinner = int(input())
hours = int(input())

handyman_bill = (((cling_film * cling_film_sq_m)
                  + (paint * paint_per_liter)
                  + (thinner * thinner_per_litter)
                  + bags) * hours) * 0.30

final_bill = (cling_film * cling_film_sq_m)\
             + (paint * paint_per_liter)\
             + (thinner * thinner_per_litter)\
             + handyman_bill\
             + 0.40

print(final_bill)


# 1. Брой страници в текущата книга – цяло число в интервала [1…1000]
# 2. Страници, които прочита за 1 час – цяло число в интервала [1…1000]
# 3. Броят на дните, за които трябва да прочете книгата – цяло число в интервала [1…1000]

# pages = int(input())
# pages_per_hour = int(input())
# days = int(input())
#
# # Formula
# hours_needed_per_day = (pages // pages_per_hour) / days
# print(int(hours_needed_per_day))

# 5. Учебни материали

# · Брой пакети химикали - цяло число в интервала [0...100]
# · Брой пакети маркери - цяло число в интервала [0...100]
# · Литри препарат за почистване на дъска - цяло число в интервала [0…50]
# · Процент намаление - цяло число в интервала [0...100]

# pens = int(input())
# markers = int(input())
# litres = int(input())
# discount = int(input())
#
# PENS_PRICE = 5.80
# MARKERS_PRICE = 7.20
# DETERGENT_PRICE = 1.20
#
# discount_amount = ((pens * PENS_PRICE)
#                    + (markers * MARKERS_PRICE)
#                    + (litres * DETERGENT_PRICE))\
#                   * (discount / 100)
#
# school_sum = ((pens * PENS_PRICE) + (markers * MARKERS_PRICE) + (litres * DETERGENT_PRICE
#                                                                  )) - discount_amount
# print(school_sum)
