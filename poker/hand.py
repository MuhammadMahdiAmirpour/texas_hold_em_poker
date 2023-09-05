from poker.validators import (
        NoCardsValidator,
        HighCardValidator,
        PairValidator,
        TwoPairValidator,
        ThreeOfAKindValidator,
        StraightValidator,
        FlushValidator,
        FullHouseValidator,
        FourOfAKindValidator,
        StraightFlushValidator,
        RoyalFlushValidator,
        )

class Hand(object):
    def __init__(self) -> None:
        self._cards = []

    def __repr__(self) -> str:
        return ", ".join([str(card) for card in self.cards])

    @property
    def _rank_validations_from_best_to_worst(self) -> tuple:
        """The _rank_validations_from_best_to_worst property."""
        return (
                ("Royal Flush", RoyalFlushValidator(cards = self.cards).is_valid),
                ("Straight Flush", StraightFlushValidator(cards = self.cards).is_valid),
                ("Four Of A Kind", FourOfAKindValidator(cards = self.cards).is_valid),
                ("Full House", FullHouseValidator(cards = self.cards).is_valid),
                ("Flush", FlushValidator(cards = self.cards).is_valid),
                ("Straight", StraightValidator(cards = self.cards).is_valid),
                ("Three Of A Kind", ThreeOfAKindValidator(cards = self.cards).is_valid),
                ("Two Pair", TwoPairValidator(cards = self.cards).is_valid),
                ("Pair", PairValidator(cards = self.cards).is_valid),
                ("High Card", HighCardValidator(cards = self.cards).is_valid),
                ("No Cards", NoCardsValidator(cards = self.cards).is_valid),
            )

    @property
    def cards(self):
        """The cards property."""
        return self._cards
    @cards.setter
    def cards(self, value):
        self._cards = value


    def best_rank(self) -> str:
        for name, validator_func in self._rank_validations_from_best_to_worst:
            if validator_func():
                return name

    def add_cards(self, cards) -> None:
        cards_copy = self.cards[:]
        cards_copy.extend(cards)
        cards_copy.sort()
        self.cards = cards_copy

