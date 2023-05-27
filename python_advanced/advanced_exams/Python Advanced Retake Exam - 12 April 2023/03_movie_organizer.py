def movie_organizer(*args):
    result = ""

    movies_dict = {}

    for movie_name, genre in args:
        if genre not in movies_dict:
            movies_dict[genre] = [movie_name]

        else:
            movies_dict[genre].append(movie_name)

    for genre_type, list_of_movies in movies_dict.items():
        movies_dict[genre_type] = sorted(list_of_movies)

    sorted_movies = sorted(movies_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    for g, m in sorted_movies:
        result += f"{g} - {len(m)}\n"
        result += '\n'.join([f"* {el}" for el in m]) + "\n"

    return result


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
