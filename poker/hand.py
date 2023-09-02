class Hand(object):
    def __init__(self, cards: list) -> None:
        cards_copy = cards[:]
        cards_copy.sort()
        self._cards = cards_copy

    @property
    def _rank_validations_from_best_to_worst(self):
        """The _rank_validations_from_best_to_worst property."""
        return (
#                 ("Flush", self._flush),
                ("Straight", self._straight),
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

    def _straight(self):
        if len(self.cards) != 5:
            return False
        for index in range(4):
            if self.cards[index + 1].rank_index - self.cards[index].rank_index != 1:
                return False
        return True
#         rank_indexes = [card.rank_index for  card in self.cards]
#         starting_rank_index = rank_indexes[0]
#         last_rank_index = rank_indexes[-1]
#         striaght_consecutive_indexes = list(
#                 range(starting_rank_index, last_rank_index + 1)
#                 )
#         return all([rank_indexes == striaght_consecutive_indexes,
#                     len(rank_indexes) == len(striaght_consecutive_indexes) == 5])

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

