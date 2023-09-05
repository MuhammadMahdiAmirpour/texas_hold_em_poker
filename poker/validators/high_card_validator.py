from poker.validators import Validator

class HighCardValidator(Validator):
    def __init__(self, cards) -> None:
        super().__init__(cards)
        self._name = "High Card"

    def is_valid(self) -> bool:
        return len(self.cards) >= 2

    def valid_cards(self):
        return self.cards[-1:]

