import unittest
from poker.card import Card

class CardTest(unittest.TestCase):

    def test_has_rank(self):
        card = Card(rank = "Queen", suit = "Hearts")
        self.assertEqual(card.rank, "Queen")

    def test_has_suit(self):
        card = Card(rank = "2", suit = "Clubs")
        self.assertEqual(card.suit, "Clubs")

    def test_has_string_representation_with_rank_and_suit(self):
        card = Card(rank = "5", suit = "Dimonds")
        self.assertEqual(str(card), "5 of Dimonds")

    def test_has_technical_representation(self):
        card = Card(rank = "5", suit = "Dimonds")
        self.assertEqual(repr(card), "Card('5', 'Dimonds')")

