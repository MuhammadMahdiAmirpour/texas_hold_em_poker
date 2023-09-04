class Hand(object):
    def __init__(self) -> None:
        self._cards = []

    def __repr__(self) -> str:
        return ", ".join([str(card) for card in self.cards])

    @property
    def _rank_validations_from_best_to_worst(self) -> tuple:
        """The _rank_validations_from_best_to_worst property."""
        return (
                ("Royal Flush", self._royal_flush),
                ("Straight Flush", self._straight_flush),
                ("Four Of A Kind", self._four_of_a_kind),
                ("Full House", self._full_house),
                ("Flush", self._flush),
                ("Straight", self._straight),
                ("Three Of A Kind", self._three_of_a_kind),
                ("Two Pair", self._two_pair),
                ("Pair", self._pair),
                ("High Card", self._high_card),
                ("No Cards", self._no_cards),
            )

    @property
    def _card_suit_counts(self):
        card_suit_counts = {}
        for card in self.cards:
            card_suit_counts.setdefault(card.suit, 0)
            card_suit_counts[card.suit] += 1
        return card_suit_counts

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

    def _royal_flush(self) -> bool:
        if len(self.cards) == 0: return False
        return all([self._straight_flush(), self.cards[-1].rank == "Ace"])

    def _straight_flush(self) -> bool:
        return all([self._straight(), self._flush()])

    def _four_of_a_kind(self) -> bool:
        ranks_with_four_of_a_kind = self._ranks_with_count(4)
        if len(ranks_with_four_of_a_kind) == 1:
            return True

    def _full_house(self) -> bool:
        return all([self._three_of_a_kind(), self._pair()])

    def _flush(self) -> bool:
        suits_that_occur_5_or_more_times = {
                suit: suit_count
                for suit, suit_count in self._card_suit_counts.items()
                if suit_count >= 5
                }
        return len(suits_that_occur_5_or_more_times) == 1

    def _straight(self) -> bool:
        if len(self.cards) < 5:
            return False
        for index in range(4):
            if self.cards[index + 1].rank_index - self.cards[index].rank_index != 1:
                return False
        return True

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
        return len(self.cards) >= 2

    def _no_cards(self) -> bool:
        return len(self.cards) == 0

    def best_rank(self) -> str:
        for name, validator_func in self._rank_validations_from_best_to_worst:
            if validator_func():
                return name

    def _ranks_with_count(self, count) -> dict:
        return {
                rank: rank_count
                for rank, rank_count in self._card_rank_counts.items()
                if rank_count == count
                }
    
    def add_cards(self, cards) -> None:
        cards_copy = cards[:]
        cards_copy.sort()
        self.cards.extend(cards_copy)

