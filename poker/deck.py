import random

class Deck(object):
    def __init__(self) -> None:
        self._cards = []
        
    @property
    def cards(self):
        """The cards property."""
        return self._cards
    
    def add_cards(self, cards: list) -> None:
        self.cards.extend(cards)

    def create_cards(self, cards) -> None:
        cards = []
        self.add_cards(cards)

    def shuffle(self) -> None:
        random.shuffle(self.cards)

