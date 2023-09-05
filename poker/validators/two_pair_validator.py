from poker.validators import Validator

class TwoPairValidator(Validator):
    def __init__(self, cards: list) -> None:
        super().__init__(cards)
        self._name = "Two Pair"

    def valid_cards(self):
        ranks_with_pairs = self._ranks_with_count(2)
        cards = [card for card in self.cards if card.rank in ranks_with_pairs.keys()]
        return cards

    def is_valid(self) -> bool:
        ranks_with_pairs = self._ranks_with_count(2)
        return len(ranks_with_pairs) == 2

