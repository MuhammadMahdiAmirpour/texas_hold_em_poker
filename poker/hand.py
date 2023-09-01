class Hand(object):
    def __init__(self, cards: list) -> None:
        cards_copy = cards[:]
        cards_copy.sort()
        self._cards = cards_copy

    @property
    def _rank_validations_from_best_to_worst(self):
        """The _rank_validations_from_best_to_worst property."""
        return (
                ("Three Of A Kind", self._three_of_a_kind),
                ("Two Pair", self._two_pair),
                ("Pair", self._pair),
                ("High Card", self._high_card),
            )

    @property
    def _card_rank_counts(self):
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

    def _three_of_a_kind(self) -> bool:
        ranks_with_three_of_a_kind = self._ranks_with_count(3)
        if len(ranks_with_three_of_a_kind) == 1:
            return True

    def _two_pair(self) -> bool:
        ranks_with_pairs = self._ranks_with_count(2)
        return len(ranks_with_pairs) == 2

    def _pair(self) -> bool:
        ranks_with_pairs = self._ranks_with_count(2)
        return len(ranks_with_pairs) == 1

    def _high_card(self) -> bool:
        return True

    def best_rank(self):
        for name, validator_func in self._rank_validations_from_best_to_worst:
            if validator_func():
                return name

    def _ranks_with_count(self, count):
        return {
                rank: rank_count
                for rank, rank_count in self._card_rank_counts.items()
                if rank_count == count
                }

