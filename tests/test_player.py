import unittest
from unittest.mock import MagicMock

from poker.card import Card
from poker.hand import Hand
from poker.player import Player

class TestPlayer(unittest.TestCase):
    def test_stores_name_and_cards(self):
        hand = Hand()
        player = Player(name = "Muhammad", hand = hand)
        self.assertEqual(
                player.name,
                "Muhammad"
                )
        self.assertEqual(
                player.hand,
                hand
                )

    def test_figures_out_own_best_hand(self):
        mock_hand = MagicMock()
        mock_hand.best_rank.return_value = "Straight Flush"
        player = Player(name = "Muhammad", hand = mock_hand)
        self.assertEqual(
            player.best_hand(),
            "Straight Flush"
        )
        mock_hand.best_rank.assert_called()

    def test_passes_new_cards_to_hand(self):
        mock_hand = MagicMock()
        player = Player(name = "Kimberly", hand = mock_hand)
        cards = [
                Card(rank = "Ace", suit = "Spades"),
                Card(rank = "Queen", suit = "Diamonds"),
                ]
        player.add_cards(cards)
        mock_hand.add_cards.assert_called_once_with(cards)

if __name__ == "__main__":
    unittest.main()

