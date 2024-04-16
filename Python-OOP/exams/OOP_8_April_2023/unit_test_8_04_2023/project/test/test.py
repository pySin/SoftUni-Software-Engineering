from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennis(TestCase):

    def setUp(self):
        self.tennis_player = TennisPlayer("Grigor", 34, 46.5)

    # Test initialize data
    def test_if_data_initializes_correctly(self):
        self.assertEqual(self.tennis_player.name, 'Grigor')
        self.assertEqual(self.tennis_player.age, 34)
        self.assertEqual(self.tennis_player.points, 46.5)
        self.assertEqual(self.tennis_player.wins, [])

    # Test name property
    def test_if_name_returns(self):
        player_name = self.tennis_player.name
        self.assertEqual("Grigor", player_name)

    def test_if_name_accepts_value(self):
        self.tennis_player.name = "Fransois"
        self.assertEqual(self.tennis_player.name, "Fransois")

    def test_if_name_rises_if_value_short(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = "Li"
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    # Test "age" property
    def test_if_age_returns(self):
        player_age = self.tennis_player.age
        self.assertEqual(player_age, 34)

    def test_if_age_can_acquire_value(self):
        self.tennis_player.age = 35
        self.assertEqual(self.tennis_player.age, 35)

    def test_if_age_rises_if_age_less_18(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    # Test add_new_win() function
    def test_if_new_win_adds_new_tournament(self):
        self.tennis_player.add_new_win("Wimbledon")
        self.assertEqual(self.tennis_player.wins[0], "Wimbledon")

    def test_return_message_if_tournament_already_won(self):
        self.tennis_player.add_new_win("Wimbledon")
        result = self.tennis_player.add_new_win("Wimbledon")
        self.assertEqual(result, f"Wimbledon has been already added to the list of wins!")

    # Test __lt__ (Less Than) function
    def test_if_lt_can_compare_players_second_better(self):
        tennis_player2 = TennisPlayer("Novak", 38, 57.5)
        self.assertEqual(self.tennis_player < tennis_player2,
                         f'{tennis_player2.name} is a top seeded player and he/she is better than '
                         f'{self.tennis_player.name}')

    def test_if_lt_can_compare_players_first_better(self):
        tennis_player2 = TennisPlayer("Lino", 38, 31.5)
        self.assertEqual(self.tennis_player < tennis_player2,
                         f'{self.tennis_player.name} is a better player than {tennis_player2.name}')

    # Test __str__() function overload
    def test_str_phrase_with_two_wins(self):
        self.tennis_player.add_new_win("Wimbledon")
        self.tennis_player.add_new_win("Masters")
        expected_phrase = f"Tennis Player: {self.tennis_player.name}\n" \
                          f"Age: {self.tennis_player.age}\n" \
                          f"Points: {self.tennis_player.points:.1f}\n" \
                          f"Tournaments won: {', '.join(self.tennis_player.wins)}"
        self.assertEqual(self.tennis_player.__str__(), expected_phrase)



if __name__ == "__main__":
    main()
