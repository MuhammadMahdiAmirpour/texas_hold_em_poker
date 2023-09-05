from poker.validators import (
        Validator,
        StraightFlushValidator,
        )

class RoyalFlushValidator(Validator):
    def __init__(self, cards: list) -> None:
        super().__init__(cards)
        self._name = "Royal Flush"

    def is_valid(self) -> bool:
        straight_flush_validator = StraightFlushValidator(cards = self.cards)
        if straight_flush_validator.is_valid():
            straight_flush_cards = straight_flush_validator.valid_cards()
            is_royal = straight_flush_cards[-1].rank == "Ace"
            return is_royal
        return False

    def valid_cards(self):
        return StraightFlushValidator(cards = self.cards).valid_cards()

