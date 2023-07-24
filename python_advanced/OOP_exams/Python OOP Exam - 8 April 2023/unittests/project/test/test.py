from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TennisPlayerTests(TestCase):
    def setUp(self) -> None:
        self.tennis_player = TennisPlayer("Test name", 20, 50)

    def test_correct_initialization(self):
        self.assertEqual("Test name", self.tennis_player.name)
        self.assertEqual(20, self.tennis_player.age)
        self.assertEqual(50, self.tennis_player.points)
        self.assertEqual([], self.tennis_player.wins)

    def test_name_setter_with_invalid_parameters_raises_correct_message(self):
        with self.assertRaises(ValueError) as ex:
            TennisPlayer("aa", 20, 50)

        expected_message = "Name should be more than 2 symbols!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_age_setter_with_invalid_parameters_raises_correct_message(self):
        with self.assertRaises(ValueError) as ex:
            TennisPlayer("test name", 15, 50)

        expected_message = "Players must be at least 18 years of age!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_get_name_return_correct_data(self):
        result = self.tennis_player.name
        self.assertEqual("Test name", result)

    def test_get_age_return_correct_name(self):
        result = self.tennis_player.age
        self.assertEqual(20, result)

    def test_add_new_win_with_new_tournament(self):
        self.tennis_player.add_new_win("new tournament")
        self.assertEqual(["new tournament"], self.tennis_player.wins)

    def test_add_new_win_with_already_won_tournament(self):
        self.tennis_player.wins = ["test tournament"]
        result = self.tennis_player.add_new_win("test tournament")
        expected = "test tournament has been already added to the list of wins!"
        self.assertEqual(expected, result)

    def test_first_player_has_less_points_then_second(self):
        second_tennis_player = TennisPlayer("Other", 20, 60)
        result = self.tennis_player < second_tennis_player
        expected_message = 'Other is a top seeded player and he/she is better than Test name'
        self.assertEqual(expected_message, result)

    def test_first_player_has_more_points_then_second(self):
        second_tennis_player = TennisPlayer("Other", 20, 40)
        result = self.tennis_player < second_tennis_player
        expected_message = 'Test name is a better player than Other'
        self.assertEqual(expected_message, result)

    def test_string_method_return_correct_message(self):
        self.tennis_player.wins = ["first tournament", "second tournament"]
        result = str(self.tennis_player)
        expected_message = "Tennis Player: Test name\n" \
               "Age: 20\n" \
               "Points: 50.0\n" \
               "Tournaments won: first tournament, second tournament"

        self.assertEqual(expected_message, result)

if __name__ == "__main__":
    main()





