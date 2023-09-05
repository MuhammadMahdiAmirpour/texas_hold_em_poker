from poker.validators import ParentStraightValidator

class StraightFlushValidator(ParentStraightValidator):

    def __init__(self, cards) -> None:
        super().__init__(cards)
        self._name = "Straight Flush"
 
    def is_valid(self) -> bool:
        for five_cards in self._batch_of_straight_cards:
            unique_suits_in_the_next_five_cards = {card.suit for card in five_cards}
            if len(unique_suits_in_the_next_five_cards) == 1:
                return True
        return False

    def valid_cards(self) -> list:
        return self._batch_of_straight_cards[-1]

