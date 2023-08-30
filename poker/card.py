class Card(object):

    @classmethod
    def validate_suit(cls, suit: str) -> bool:
        pass

    @classmethod
    def validate_rank(cls, rank: str) -> bool:
        pass

    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit

    @property
    def rank(self):
        """The rank property."""
        return self._rank
    @rank.setter
    def rank(self, value):
        self._rank = value

    @property
    def suit(self):
        """The suit property."""
        return self._suit
    @suit.setter
    def suit(self, value):
        self._suit = value

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def __repr__(self) -> str:
        return f"Card('{self.rank}', '{self.suit}')"

