from typing import List
from project.movie_specification.movie import Movie
from project.user import User

class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def __str__(self) -> str:
        users = ", ".join([u.username for u in self.users_collection]) if self.users_collection else "No users."
        movies = ", ".join([m.title for m in self.movies_collection]) if self.movies_collection else "No movies."
        return f"All users: {users}\nAll movies: {movies}"

    def register_user(self, username: str, age: int) -> str:
        if self._find_user_by_name(username) is not None:
            raise Exception("User already exists!")

        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie) -> str:
        user = self._find_user_by_name(username)
        self._upload_movie_validator(user, movie)
        self.movies_collection.append(movie)
        user.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."


    def edit_movie(self, username: str, movie: Movie, **kwargs) -> str:
        user = self._find_user_by_name(username)
        self._edit_movie_validator(user, movie)

        for key, value in kwargs.items():
            if key == "title":
                movie.title = value
            elif key == "year":
                movie.year = value
            elif key == "age_restriction":
                movie.age_restriction = value

        return f"{user.username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie) -> str:
        user = self._find_user_by_name(username)
        self._delete_movie_validator(user, movie)
        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie) -> str:
        user = self._find_user_by_name(username)
        self._like_movie_validator(user, movie)
        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie) -> str:
        user = self._find_user_by_name(username)
        self._dislike_validator(user, movie)
        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self) -> str:
        if not self.movies_collection:
            return "No movies found."

        return "\n".join([m.details() for m in sorted(self.movies_collection, key=lambda x: (-x.year, x.title))])


    def _find_user_by_name(self, name):
        user = [u for u in self.users_collection if u.username == name]
        if user:
            return user[0]

    def _edit_movie_validator(self, user: User, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner != user:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")

    def _upload_movie_validator(self, user: User, movie: Movie):
        if user is None:
            raise Exception("This user does not exist!")
        if movie.owner != user:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

    def _delete_movie_validator(self, user: User, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner != user:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")

    @staticmethod
    def _like_movie_validator(user: User, movie: Movie):
        if movie.owner == user:
            raise Exception(f"{user.username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{user.username} already liked the movie {movie.title}!")

    @staticmethod
    def _dislike_validator(user: User, movie: Movie):
        if movie not in user.movies_liked:
            raise Exception(f"{user.username} has not liked the movie {movie.title}!")













