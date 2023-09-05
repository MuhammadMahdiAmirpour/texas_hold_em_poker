class Validator(object):

    def __init__(self, cards: list) -> None:
        cards_copy = cards[:]
        cards_copy.sort()
        self._cards = cards_copy

    def _ranks_with_count(self, count) -> dict:
        return {
                rank: rank_count
                for rank, rank_count in self._card_rank_counts.items()
                if rank_count == count
                }

    @property
    def _card_rank_counts(self) -> dict:
        """The _card_rank_counts property."""
        card_rank_counts = {}
        for card in self.cards:
            card_rank_counts.setdefault(card.rank, 0)
            card_rank_counts[card.rank] += 1
        return card_rank_counts

    @property
    def cards(self):
        """The cards property."""
        return self._cards
    @cards.setter
    def cards(self, value):
        self._cards = value

    @property
    def name(self):
        """The name property."""
        return self._name


