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
        self.deck.shuffle()
        for player in self.players:
            self.deck.remove_cards(2)

