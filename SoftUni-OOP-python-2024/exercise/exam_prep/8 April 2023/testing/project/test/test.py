from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):

    def setUp(self) -> None:
        self.tennis_player = TennisPlayer("grisho", 20, 50)

    def test_init(self):
        self.assertEqual("grisho", self.tennis_player.name)
        self.assertEqual(20, self.tennis_player.age)
        self.assertEqual(50, self.tennis_player.points)

    def test_name_setter_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = "gr"
        result_message = "Name should be more than 2 symbols!"
        self.assertEqual(result_message, str(ve.exception))

    def test_age_setter_expect_value_error(self):
        result_message = "Players must be at least 18 years of age!"
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.age = 15

        self.assertEqual(result_message, str(ve.exception))

    def test_add_new_win_tournament_already_added(self):
        self.tennis_player.wins = ["Sofia"]

        result_message = "Sofia has been already added to the list of wins!"
        result_action = self.tennis_player.add_new_win("Sofia")
        self.assertEqual(result_message, result_action)

    def test_add_new_win_success(self):
        self.tennis_player.add_new_win("Sofia")
        self.assertEqual("Sofia", self.tennis_player.wins[-1])

    def test_lt_method_tennis_player_has_less_points_than_other(self):
        self.second_player = TennisPlayer("gosho", 20, 60)
        result_message = f'gosho is a top seeded player and he/she is better than grisho'
        result_action = self.tennis_player.__lt__(self.second_player)

        self.assertEqual(result_message, result_action)

    def test_lt_method_first_player_has_mre_points(self):
        self.second_player = TennisPlayer("gosho", 20, 10)
        result_message = f'grisho is a better player than gosho'
        result_action = self.tennis_player.__lt__(self.second_player)

        self.assertEqual(result_message, result_action)

    def test_str_method_without_tournaments(self):
        result_message = f"Tennis Player: {self.tennis_player.name}\n" \
               f"Age: 20\n" \
               f"Points: 50.0\n" \
               f"Tournaments won: "

        self.assertEqual(result_message, self.tennis_player.__str__())

    def test_str_method_with_tournaments(self):
        self.tennis_player.wins = ["1", "2"]
        result_message = f"Tennis Player: grisho\n" \
                         f"Age: 20\n" \
                         f"Points: 50.0\n" \
                         f"Tournaments won: 1, 2"
        self.assertEqual(result_message, self.tennis_player.__str__())


if __name__ == "__main__":
    main()