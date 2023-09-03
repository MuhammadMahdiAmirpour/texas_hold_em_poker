import unittest
from unittest.mock import MagicMock
from poker.hand import Hand
from poker.player import Player

class TestPlayer(unittest.TestCase):
    def test_stores_name_and_cards(self):
        hand = Hand(cards = [])
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

if __name__ == "__main__":
    unittest.main()

