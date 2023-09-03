import random

class Deck(object):
    def __init__(self) -> None:
        self._cards = []

    def __len__(self) -> int:
        return len(self.cards)

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

    def remove_cards(self, number: int) -> list:
        cards_to_remove = self.cards[:number]
        del self.cards[:number]
        return cards_to_remove

