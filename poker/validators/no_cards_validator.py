from poker.validators import Validator

class NoCardsValidator(Validator):

    def __init__(self, cards) -> None:
        super().__init__(cards)
        self._name = "No Cards"

    def is_valid(self):
        return len(self.cards) == 0
        
    def valid_cards(self):
        return self.cards

