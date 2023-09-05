import unittest

from poker.card import Card
from poker.validators import ThreeOfAKindValidator

class ThreeOfAKindValidatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.five_of_clubs = Card(rank = "5", suit = "Clubs")
        self.king_of_clubs = Card(rank = "King", suit = "Clubs")
        self.king_of_diamonds = Card(rank = "King", suit = "Diamonds")
        self.king_of_hearts = Card(rank = "King", suit = "Hearts")
        self.ace_fo_spaces = Card(rank = "Ace", suit = "Spades")
        self.cards = [
                self.five_of_clubs,
                self.king_of_clubs,
                self.king_of_diamonds,
                self.king_of_hearts,
                self.ace_fo_spaces,
               ]
 

    def test_figures_out_three_of_a_king_is_best_rank(self):
        validator = ThreeOfAKindValidator(cards = self.cards)
        self.assertEqual(
                validator.is_valid(),
                True
                )

    def test_returns_three_of_a_kind_cards_from_card_collection(self):
        validator = ThreeOfAKindValidator(cards = self.cards)
        self.assertEqual(
                validator.valid_cards(),
                [
                    self.king_of_clubs,
                    self.king_of_diamonds,
                    self.king_of_hearts,
                    ]
                )

