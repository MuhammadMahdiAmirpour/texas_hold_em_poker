from poker.validators import (
        RoyalFlushValidator,
        StraightFlushValidator,
        FourOfAKindValidator,
        FullHouseValidator,
        FlushValidator,
        StraightValidator,
        ThreeOfAKindValidator,
        TwoPairValidator,
        PairValidator,
        HighCardValidator,
        NoCardsValidator,
        )

class Hand(object):
    def __init__(self) -> None:
        self._cards = []

    def __repr__(self) -> str:
        return ", ".join([str(card) for card in self.cards])

    VALIDATORS = (
        RoyalFlushValidator,
        StraightFlushValidator,
        FourOfAKindValidator,
        FullHouseValidator,
        FlushValidator,
        StraightValidator,
        ThreeOfAKindValidator,
        TwoPairValidator,
        PairValidator,
        HighCardValidator,
        NoCardsValidator,
            )

    def best_rank(self) -> str:
        for index, validator_klass in enumerate(self.VALIDATORS):
            validator = validator_klass(cards = self.cards)
            if validator.is_valid():
                return (index, validator.name, validator.valid_cards())

    @property
    def cards(self):
        """The cards property."""
        return self._cards
    @cards.setter
    def cards(self, value):
        self._cards = value

    def add_cards(self, cards) -> None:
        cards_copy = self.cards[:]
        cards_copy.extend(cards)
        cards_copy.sort()
        self.cards = cards_copy

