import unittest

from poker.card import Card
from poker.validators import RoyalFlushValidator

class StraightFlushValidatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.ten_of_clubs = Card(rank = "10", suit = "Clubs")
        self.jack_of_clubs = Card(rank = "Jack", suit = "Clubs")
        self.queen_of_clubs = Card(rank = "Queen", suit = "Clubs")
        self.king_of_clubs = Card(rank = "King", suit = "Clubs")
        self.ace_of_clubs = Card(rank = "Ace", suit = "Clubs")
        self.base_cards = [
                self.ten_of_clubs,
                self.jack_of_clubs,
                self.queen_of_clubs,
                self.king_of_clubs,
                self.ace_of_clubs,
                ]
        self.first_card_sample = [
                Card(rank = "9", suit = "Clubs"),
                self.ten_of_clubs,
                self.jack_of_clubs,
                self.queen_of_clubs,
                self.king_of_clubs,
                Card(rank = "Ace", suit = "Diamonds"),
                ]
        self.second_card_sample = [
                Card(rank = "2", suit = "Spades"),
                self.ten_of_clubs,
                self.jack_of_clubs,
                self.queen_of_clubs,
                self.king_of_clubs,
                self.ace_of_clubs,
                Card(rank = "Ace", suit = "Diamonds"),
                ]

    def test_validates_that_cards_do_not_have_straight_flush_ending_in_ace(self):
        validator = RoyalFlushValidator(cards = self.first_card_sample)
        print(validator.valid_cards())
        self.assertEqual(
                validator.is_valid(),
                False
                )

    def test_validates_that_cards_do_not_have_straight_flush_ending_in_ace(self):
        validator = RoyalFlushValidator(cards = self.second_card_sample)
        self.assertEqual(
                validator.is_valid(),
                True
                )

    def test_returns_five_straight_cards_with_same_rank_ending_with_ace(self):
        validator = RoyalFlushValidator(cards = self.second_card_sample)
        self.assertEqual(
                validator.valid_cards(),
                [
                self.ten_of_clubs,
                self.jack_of_clubs,
                self.queen_of_clubs,
                self.king_of_clubs,
                self.ace_of_clubs,
                    ]
                )

