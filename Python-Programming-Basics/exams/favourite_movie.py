# Favourite Movie

movie_name = ""
top_movie_points = 0

x = 0
while True:
    x += 1

    current_movie_name = input()

    if current_movie_name == "STOP":
        break

    movie_result = 0
    for letter in current_movie_name:
        movie_result += ord(letter)
        if 97 <= ord(letter) <= 122:
            movie_result -= len(current_movie_name) * 2
        elif 65 <= ord(letter) <= 90:
            movie_result -= len(current_movie_name)

    if movie_result > top_movie_points:
        top_movie_points = movie_result
        movie_name = current_movie_name

    if x == 7:
        print(f"The limit is reached.")
        break

print(f"The best movie for you is {movie_name} with {top_movie_points} ASCII sum.")
