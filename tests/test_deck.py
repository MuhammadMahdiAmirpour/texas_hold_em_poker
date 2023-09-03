import unittest
from unittest.mock import patch

from poker.card import Card
from poker.deck import Deck

class DeckTest(unittest.TestCase):
    def test_stores_no_cards_at_start(self):
        deck = Deck()
        self.assertEqual(
                deck.cards,
                []
                )
    
    def test_adds_cards_to_its_collection(self):
        card = Card(rank = "Ace", suit = "Spades")
        deck = Deck()
        deck.add_cards([card])
        self.assertEqual(
                deck.cards,
                [card]
                )

    @patch('random.shuffle')
    def test_shuffles_cards_in_random_order(self, mock_shuffle):
        deck = Deck()
        cards = [
                Card(rank = "Ace", suit = "Spades"),
                Card(rank = "8", suit = "Diamonds"),
                ]
        deck.add_cards(cards)
        deck.shuffle()
        mock_shuffle.assert_called_once_with(cards)

    def test_removes_specific_number_of_cards_from_deck(self):
        ace_of_spades = Card(rank = "Ace", suit = "Spades")
        eight_of_diamonds = Card(rank = "8", suit = "Diamonds")
        cards = [ace_of_spades, eight_of_diamonds]
        deck = Deck()
        deck.add_cards(cards)
        self.assertEqual(
                deck.remove_cards(1),
                [ace_of_spades]
                )
        self.assertEqual(
                deck.cards,
                [eight_of_diamonds]
                )

if __name__ == "__main__":
    unittest.main()

