import unittest

from poker.card import Card
from poker.validators import StraightValidator

class StraightValidtorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.two_of_spades = Card(rank = "2", suit = "Spades")
        self.ten_of_clubs = Card(rank = "10", suit = "Clubs")
        self.six_of_hearts = Card(rank = "6", suit = "Hearts")
        self.nine_of_clubs = Card(rank = "9", suit = "Clubs")
        self.jack_of_hearts = Card(rank = "Jack", suit = "Hearts")
        self.eight_of_spades = Card(rank = "8", suit = "Spades")
        self.seven_of_diamonds = Card(rank = "7", suit = "Diamonds")
        self.first_cards = [
                    self.two_of_spades,
                    self.ten_of_clubs,
                    self.six_of_hearts,
                    self.nine_of_clubs,
                    self.jack_of_hearts,
                    self.eight_of_spades,
                    self.seven_of_diamonds,
                ]
        self.king_of_clubs = Card(rank = "King", suit = "Clubs")
        self.ace_of_hearts = Card(rank = "Ace", suit = "Hearts")
        self.queen_of_clubs = Card(rank = "Queen", suit = "Clubs")
        self.jack_of_spades = Card(rank = "Jack", suit = "Spades")
        self.ten_of_diamonds = Card(rank = "10", suit = "Diamonds")
        self.second_cards = [
                    self.king_of_clubs,
                    self.ace_of_hearts,
                    self.queen_of_clubs,
                    self.jack_of_spades,
                    self.ten_of_diamonds, 
                ]
        self.two_sequential_cards = [
                    self.six_of_hearts,
                    self.seven_of_diamonds,
                ]

    def test_determindes_if_there_is_five_cards_in_a_row(self):
        validator = StraightValidator(cards = self.first_cards)
        self.assertEqual(
                validator.is_valid(),
                True
                )
        validator = StraightValidator(cards = self.second_cards)
        self.assertEqual(
                validator.is_valid(),
                True
                )

    def test_does_not_seem_two_consecutive_cards_as_straight(self):
        validator = StraightValidator(cards = self.two_sequential_cards)
        self.assertEqual(
                validator.is_valid(),
                False
                )

