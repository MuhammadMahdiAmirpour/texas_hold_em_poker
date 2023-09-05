from poker.validators import ParentStraightValidator

class StraightValidator(ParentStraightValidator):
    def __init__(self, cards) -> None:
        super().__init__(cards)
        self._name = "Straight"

    def is_valid(self) -> bool:
        if len(self.cards) < 5:
            return False
        return len(self._batch_of_straight_cards) >= 1

    def valid_cards(self) -> list:
        return self._batch_of_straight_cards[-1]

