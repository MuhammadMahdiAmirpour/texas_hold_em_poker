from poker.validators import (
        ThreeOfAKindValidator,
        PairValidator,
        Validator,
        )

class FullHouseValidator(Validator):
    def __init__(self, cards) -> None:
        super().__init__(cards)
        self._name = "Full House"

    def is_valid(self) -> bool:
        return all([ThreeOfAKindValidator(cards = self.cards),
                    PairValidator(cards = self.cards).is_valid()])

    def valid_cards(self) -> list:
        return ThreeOfAKindValidator(cards = self.cards).valid_cards() + \
                PairValidator(cards = self.cards).valid_cards()

