from poker.validators import Validator

class ThreeOfAKindValidator(Validator):
    def __init__(self, cards) -> None:
        super().__init__(cards)
        self._name = "Three Of A Kind"

    def is_valid(self):
        ranks_with_three_of_a_kind = self._ranks_with_count(3)
        return len(ranks_with_three_of_a_kind) == 1
        
        
    def valid_cards(self):
        ranks_with_three_of_a_kind = self._ranks_with_count(3)
        cards = [card for card in self.cards if card.rank in ranks_with_three_of_a_kind.keys()]
        return cards
 
