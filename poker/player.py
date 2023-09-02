class Player(object):
    def __init__(self, name, hand) -> None:
        self._name = name
        self._hand = hand
        
    @property
    def name(self) -> str:
        """The name property."""
        return self._name

    @property
    def hand(self) -> list:
        """The hand property."""
        return self._hand

    def best_hand(self):
        self.hand.best_rank()

