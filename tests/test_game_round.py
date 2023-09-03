import unittest
from unittest.mock import MagicMock
from unittest.mock import call

from poker.game_round import GameRound

class GameRoundTest(unittest.TestCase):
    def test_store_deck_palyers(self):
        mock_deck = MagicMock()
        players = [
                MagicMock(),
                MagicMock(),
                ]
        game_round = GameRound(
                deck = mock_deck,
                players = players
                )
        self.assertEqual(
                game_round.deck,
                mock_deck
                )
        self.assertEqual(
                game_round.players,
                players
                )
    
    def test_game_play_shuffles_deck(self):
        mock_deck = MagicMock()
        players = [
                MagicMock(),
                MagicMock(),
                ]
        game_round = GameRound(
                deck = mock_deck,
                players = players
                )
        game_round.play()
        mock_deck.shuffle.assert_called_once()

    def test_deals_two_initial_cards_from_deck_to_each_player(self):
        mock_deck = MagicMock()
        players = [
                MagicMock(),
                MagicMock(),
                ]
        game_round = GameRound(
                deck = mock_deck,
                players = players
                )
        game_round.play()
        mock_deck.remove_cards.assert_has_calls([
            call(2), call(2)
            ])

if __name__ == "__main__":
    unittest.main()

