import unittest

from poker.card import Card
from poker.validators import StraightFlushValidator

class StraightFlushValidatorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.three_of_clubs = Card(rank = "3", suit = "Clubs")
        self.four_of_clubs = Card(rank = "4", suit = "Clubs")
        self.five_of_clubs = Card(rank = "5", suit = "Clubs")
        self.six_of_clubs = Card(rank = "6", suit = "Clubs")
        self.seven_of_clubs = Card(rank = "7", suit = "Clubs")
        self.base_cards = [
                     self.three_of_clubs,
                     self.four_of_clubs,
                     self.five_of_clubs, 
                     self.six_of_clubs,
                     self.seven_of_clubs,
                      ]
        self.first_card_samples = [
                     self.three_of_clubs,
                     self.four_of_clubs,
                     self.five_of_clubs, 
                     self.six_of_clubs,
                     Card(rank = "7", suit = "Diamonds"),
                     Card(rank = "King", suit = "Clubs"),
                     Card(rank = "Ace", suit = "Diamonds"),
                      ]
        self.second_card_samples = [
                     self.three_of_clubs,
                     self.four_of_clubs,
                     self.five_of_clubs, 
                     self.six_of_clubs,
                     Card(rank = "7", suit = "Clubs"),
                     self.seven_of_clubs,
                     Card(rank = "King", suit = "Clubs"),
                     Card(rank = "Ace", suit = "Diamonds"),
                      ]

    def test_determines_that_there_are_not_five_consecutive_cards_with_the_same_suit(self):
        validator = StraightFlushValidator(cards = self.first_card_samples)
        self.assertEqual(
                validator.is_valid(),
                False
                )

    def test_determines_that_there_are_five_consecutive_cards_with_the_same_suit(self):
        validator = StraightFlushValidator(cards = self.second_card_samples)
        self.assertEqual(
                validator.is_valid(),
                True
                )
 
