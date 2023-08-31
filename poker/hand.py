class Hand(object):
    def __init__(self, cards: list) -> None:
        self._cards = cards

    @property
    def cards(self):
        """The cards property."""
        return self._cards
    @cards.setter
    def cards(self, value):
        self._cards = value

    def best_rank(self):
        return "High Card"

