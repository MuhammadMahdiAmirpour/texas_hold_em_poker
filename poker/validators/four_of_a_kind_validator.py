from poker.validators import Validator

class FourOfAKindValidator(Validator):
    def __init__(self, cards) -> None:
        super().__init__(cards)
        self._name = "Four Of A Kind"

    def is_valid(self) -> bool:
        ranks_with_four_of_a_kind = self._ranks_with_count(4)
        if len(ranks_with_four_of_a_kind) == 1:
            return True

    def valid_cards(self) -> list:
        ranks_with_four_of_a_kind = self._ranks_with_count(4)
        cards = [card for card in self.cards if card.rank in ranks_with_four_of_a_kind.keys()]
        return cards
