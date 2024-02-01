def movie_organizer(*args):
    movies = {}
    final_data = []

    for movie, genre in args:
        if genre not in movies:
            movies[genre] = []
        movies[genre].append(movie)

    sorted_genres = sorted(movies.keys())
    sorted_genres.sort(key=lambda x: (-len(movies[x]), x))

    for genre in sorted_genres:
        final_data.append(f"{genre} - {len(movies[genre])}")
        for movie in sorted(movies[genre]):
            final_data.append(f"* {movie}")

    return "\n".join(str(x) for x in final_data)



print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))
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
