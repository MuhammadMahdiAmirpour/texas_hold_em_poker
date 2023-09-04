import unittest
from unittest import mock
from unittest.mock import MagicMock
from unittest.mock import call

from poker.game_round import GameRound
from poker.card import Card

class GameRoundTest(unittest.TestCase):
    def setUp(self) -> None:
        self.first_two_cards = [
                Card(rank = "2", suit = "Hearts"),
                Card(rank = "6", suit = "Clubs"),
                ]
        self.second_two_cards = [
                Card(rank = "9", suit = "Diamonds"),
                Card(rank = "4", suit = "Spades"),
                ]
        self.flop_cards = [
                Card(rank = "2", suit = "Diamonds"),
                Card(rank = "4", suit = "Hearts"),
                Card(rank = "10", suit = "Spades"),
                ]
        self.turn_cards = [
                Card(rank = "9", suit = "Hearts")
                ]
        self.river_cards = [
                Card(rank = "Queen", suit = "Clubs")
                ]

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
        mock_deck.remove_cards.side_effect = [
                self.first_two_cards,
                self.second_two_cards,
                self.flop_cards,
                self.turn_cards,
                self.river_cards,
                ]
        mock_player1 = MagicMock()
        mock_player2 = MagicMock()
        players = [
                mock_player1,
                mock_player2,
                ]
        game_round = GameRound(
                deck = mock_deck,
                players = players
                )
        game_round.play()
        mock_deck.remove_cards.assert_has_calls([
            call(2), call(2)
            ])
        mock_player1.add_cards.assert_has_calls([
            call(self.first_two_cards)
            ])
        mock_player2.add_cards.assert_has_calls([
            call(self.second_two_cards)
            ])

    def test_removes_player_if_not_willing_to_make_bet(self):
        deck = MagicMock()
        player1 = MagicMock()
        player2 = MagicMock()
        player1.wants_to_fold.return_value = True
        player2.wants_to_fold.return_value = False
        players = [player1, player2]
        game_round = GameRound(deck = deck, players = players)
        game_round.play()
        self.assertEqual(
                game_round.players,
                [player2]
                )

    def test_deals_eack_player_3_flop_1_turn_and_1_river_cards(self):
        mock_player1 = MagicMock()
        mock_player1.wants_to_fold.return_value = False
        mock_player2 = MagicMock()
        mock_player2.wants_to_fold.return_value = False
        players = [mock_player1, mock_player2]
        mock_deck = MagicMock()
        mock_deck.remove_cards.side_effect = [
                self.first_two_cards,
                self.second_two_cards,
                self.flop_cards,
                self.turn_cards,
                self.river_cards,
                ]
        game_round = GameRound(deck = mock_deck, players = players)
        game_round.play()
        mock_deck.remove_cards.assert_has_calls([
            call(3), call(1), call(1)
            ])
        calls = [
            call(self.flop_cards),
            call(self.turn_cards),
            call(self.river_cards),
        ]
        for player in players:
            player.add_cards.assert_has_calls(calls)

if __name__ == "__main__":
    unittest.main()

