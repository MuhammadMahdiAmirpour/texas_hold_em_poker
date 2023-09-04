from poker.deck import Deck
class GameRound(object):
    def __init__(self, deck: Deck, players: list) -> None:
        self._deck = deck
        self._players = players

    @property
    def deck(self):
        """The deck property."""
        return self._deck

    @property
    def players(self):
        """The palyers property."""
        return self._players
    
    def play(self):
        self._shuffle_deck()
        self._deal_initial_two_cards_to_each_player()
        self._make_bets()
        self._deal_flop_cards()

    def _shuffle_deck(self):
        self.deck.shuffle()

    def _deal_initial_two_cards_to_each_player(self):
        for player in self.players:
            player.add_cards(self.deck.remove_cards(2))

    def _make_bets(self):
        for player in self.players:
            if player.wants_to_fold():
                self.players.remove(player)

    def _deal_flop_cards(self):
        community_cards = self.deck.remove_cards(3)
        for player in self.players:
            player.add_cards(community_cards)

