# Movie Ratings

number_of_movies = int(input())
initial_number_movies = number_of_movies
highest_rating = 0
highest_rating_movie = ""
lowest_rating = 0
lowest_rating_movie = ""
rating_sum = 0


while number_of_movies > 0:
    movie_name = input()
    movie_rating = float(input())

    if highest_rating == 0:
        highest_rating = movie_rating
        highest_rating_movie = movie_name
    elif highest_rating < movie_rating:
        highest_rating = movie_rating
        highest_rating_movie = movie_name

    if lowest_rating == 0:
        lowest_rating = movie_rating
        lowest_rating_movie = movie_name
    elif lowest_rating > movie_rating:
        lowest_rating = movie_rating
        lowest_rating_movie = movie_name

    if rating_sum == 0:
        rating_sum = movie_rating
    else:
        rating_sum = rating_sum + movie_rating

    number_of_movies -= 1

average_rating = rating_sum / initial_number_movies

print(f"{highest_rating_movie} is with highest rating: {highest_rating:.1f}")
print(f"{lowest_rating_movie} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
