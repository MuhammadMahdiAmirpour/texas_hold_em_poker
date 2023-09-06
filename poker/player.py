class Player(object):
    def __init__(self, name, hand) -> None:
        self._name = name
        self._hand = hand

    def __gt__(self, __value: object) -> bool:
        current_player_best_validator_index = self.best_hand()[0]
        other_player_best_validator_index = __value.best_hand()[0]
        if current_player_best_validator_index == other_player_best_validator_index:
            return max(self.hand.cards) > max(__value.hand.cards)
        return current_player_best_validator_index < other_player_best_validator_index

    @property
    def name(self) -> str:
        """The name property."""
        return self._name

    @property
    def hand(self) -> list:
        """The hand property."""
        return self._hand

    def best_hand(self) -> str:
        return self.hand.best_rank()

    def add_cards(self, cards: list) -> None:
        self.hand.add_cards(cards)

    def wants_to_fold(self):
        return False

