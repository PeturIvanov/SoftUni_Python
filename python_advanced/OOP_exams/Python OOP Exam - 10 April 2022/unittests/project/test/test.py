from project.movie import Movie
from unittest import TestCase, main


class MovieTests(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("Test", 2000, 90.5)

    def test_constructor(self):
        self.assertEqual("Test", self.movie.name)
        self.assertEqual(2000, self.movie.year)
        self.assertEqual(90.5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_movie_with_empty_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            Movie("", 2000, 50)
        expected_message = "Name cannot be an empty string!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_movie_with_invalid_year_raises(self):
        with self.assertRaises(ValueError) as ex:
            Movie("Error", 1886, 40)
        expected_message = "Year is not valid!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_add_new_actor(self):
        self.assertEqual([], self.movie.actors)
        result = self.movie.add_actor("Actor")
        self.assertEqual(None, result)
        self.assertEqual(["Actor"], self.movie.actors)

    def test_add_actor_that_exist(self):
        self.movie.add_actor("Actor")
        self.assertEqual(["Actor"], self.movie.actors)

        result = self.movie.add_actor("Actor")
        expected_message = "Actor is already added in the list of actors!"
        self.assertEqual(expected_message, result)
        self.assertEqual(["Actor"], self.movie.actors)

    def test_greater_then_dunder_method(self):
        second_movie = Movie("Second", 2023, 60)
        result = self.movie > second_movie
        expected = '"Test" is better than "Second"'
        self.assertEqual(expected, result)

    def test_less_then_dunder_method(self):
        second_movie = Movie("Second", 2023, 99)
        result = self.movie > second_movie
        expected = '"Second" is better than "Test"'
        self.assertEqual(expected, result)

    def test_repr_dunder_method_represent_correct(self):
        self.movie.add_actor("Actor1")
        self.movie.add_actor("Actor2")
        result = repr(self.movie)
        expected = f"Name: Test\n" \
               f"Year of Release: 2000\n" \
               f"Rating: 90.50\n" \
               f"Cast: Actor1, Actor2"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()