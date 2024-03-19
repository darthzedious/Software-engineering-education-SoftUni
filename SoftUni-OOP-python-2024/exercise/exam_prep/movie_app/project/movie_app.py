from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection: list[Movie] = []
        self.users_collection: list[User] = []

    def register_user(self, username, age):
        user = User(username, age)

        for u in self.users_collection:
            if u.username == user.username:
                raise Exception("User already exists!")
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username, movie: Movie):
        try:
            user = next(filter(lambda u: u.username == username, self.users_collection))
        except StopIteration:
            raise Exception("This user does not exist!")

        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        existing_movie = [m for m in self.movies_collection if m.title == movie.title]
        if existing_movie:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username, movie: Movie, **kwargs):
        user = next(filter(lambda u: u.username == username, self.users_collection))
        existing_movie = [m for m in self.movies_collection if m.title == movie.title]

        if movie.owner.username != user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if not existing_movie:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        for atr, value in kwargs.items():
            setattr(movie, atr, value)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username, movie: Movie):
        user = next(filter(lambda u: u.username == username, self.users_collection))
        existing_movie = [m for m in self.movies_collection if m.title == movie.title]

        if movie.owner.username != user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if not existing_movie:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username, movie: Movie):
        user = next(filter(lambda u: u.username == username, self.users_collection))

        if user.username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        existing_movie = [m for m in user.movies_liked if m.title == movie.title]

        if existing_movie:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username, movie: Movie):
        user = next(filter(lambda u: u.username == username, self.users_collection))
        existing_movie = [m for m in user.movies_liked if m.title == movie.title]

        if not existing_movie:
        #if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        user.movies_liked.remove(movie)
        movie.likes -= 1
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        uploaded_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))

        if not uploaded_movies:
            return "No movies found."
        return "\n".join([m.details() for m in uploaded_movies])

    def __str__(self):
        result = ""
        # result = ["All users:"]
        # if not self.users_collection:
        #     result.append(" No users.")
        # else:
        #     result.append([x.username for x in self.users_collection])
        # result.append("\nAll movies:")
        #
        # if not self.movies_collection:
        #     result.append(" No movies.")
        # else:
        #     result.append([x.title for x in self.movies_collection])
        #
        # return ''.join(str(x) for x in result)

        if not self.users_collection:
            result = "All users: No users.\n"
        else:
            result += "All users: " + ', '.join([x.username for x in self.users_collection]) + "\n"

        if not self.movies_collection:
            result = "All movies: No movies.\n"
        else:
            result += "All movies: " + ', '.join([x.title for x in self.movies_collection]) + "\n"

        return result
# class MovieApp:
#     def __init__(self):
#         self.movies_collection = []
#         self.users_collection = []
#
#     def check_if_user_exists(self, username):
#         for user in self.users_collection:
#             if user.username == username:
#                 return True
#         return False
#
#     def check_if_movie_exists(self, title):
#         for movie in self.movies_collection:
#             if movie.title == title:
#                 return True
#         return False
#
#     def check_if_user_liked_movie(self, username, movie_title):
#         for user in self.users_collection:
#             if user.username == username:
#                 for movie in user.movies_liked:
#                     if movie.title == movie_title:
#                         return True
#                 return False
#
#     def register_user(self, username, age):
#         if self.check_if_user_exists(username):
#             raise Exception('User already exists!')
#         new_user = User(username, age)
#         self.users_collection.append(new_user)
#         return f'{username} registered successfully.'
#
#     def upload_movie(self, username, movie):
#         if not self.check_if_user_exists(username):
#             raise Exception('This user does not exist!')
#         elif self.check_if_movie_exists(movie.title):
#             raise Exception('Movie already added to the collection!')
#         elif not username == movie.owner.username:
#             raise Exception(f'{username} is not the owner of the movie {movie.title}!')
#         else:
#             self.movies_collection.append(movie)
#             for user in self.users_collection:
#                 if user.username == username:
#                     user.movies_owned.append(movie)
#                     return f'{username} successfully added {movie.title} movie.'
#
#     def edit_movie(self, username, movie, **kwargs):
#         if not self.check_if_movie_exists(movie.title):
#             raise Exception(f'The movie {movie.title} is not uploaded!')
#         elif not username == movie.owner.username:
#             raise Exception(f'{username} is not the owner of the movie {movie.title}!')
#         else:
#             for attr, new_value in kwargs.items():
#                 setattr(movie, attr, new_value)
#             return f'{username} successfully edited {movie.title} movie.'
#
#     def delete_movie(self, username, movie):
#         if not self.check_if_movie_exists(movie.title):
#             raise Exception(f'The movie {movie.title} is not uploaded!')
#         elif not username == movie.owner.username:
#             raise Exception(f'{username} is not the owner of the movie {movie.title}!')
#         else:
#             self.movies_collection.pop(self.movies_collection.index(movie))
#             for user in self.users_collection:
#                 if user.username == username:
#                     user.movies_owned.pop(user.movies_owned.index(movie))
#                     return f'{username} successfully deleted {movie.title} movie.'
#
#     def like_movie(self, username, movie):
#         if username == movie.owner.username:
#             raise Exception(f'{username} is the owner of the movie {movie.title}!')
#         elif self.check_if_user_liked_movie(username, movie.title):
#             raise Exception(f'{username} already liked the movie {movie.title}!')
#         else:
#             movie.likes += 1
#             for user in self.users_collection:
#                 if user.username == username:
#                     user.movies_liked.append(movie)
#             return f'{username} liked {movie.title} movie.'
#
#     def dislike_movie(self, username, movie):
#         if not self.check_if_user_liked_movie(username, movie.title):
#             raise Exception(f'{username} has not liked the movie {movie.title}!')
#         else:
#             movie.likes -= 1
#             for user in self.users_collection:
#                 if user.username == username:
#                     user.movies_liked.pop(user.movies_liked.index(movie))
#             return f'{username} disliked {movie.title} movie.'
#
#     def display_movies(self):
#         if len(self.movies_collection) == 0:
#             return 'No movies found.'
#         else:
#             result_str = []
#             for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
#                 result_str.append(movie.details())
#             return '\n'.join(result_str)
#
#     def __str__(self):
#         if len(self.users_collection) == 0:
#             users = 'No users.'
#         else:
#             users = ', '.join([user.username for user in self.users_collection])
#         if len(self.movies_collection) == 0:
#             movies = 'No movies.'
#         else:
#             movies = ', '.join([movie.title for movie in self.movies_collection])
#
#         return f'All users: {users}\nAll movies: {movies}'