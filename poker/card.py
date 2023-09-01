class Card(object):

    SUITS = ("Hearts", "Clubs", "Spades", "Diamonds")

    RANKS = (
                    "2",
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                    "9",
                    "10",
                    "Jack",
                    "Queen",
                    "King",
                    "Ace",
                    )

    @classmethod
    def create_standard_52_cards(cls) -> list:
        return [
                cls(rank = rank, suit = suit)
                for suit in cls.SUITS
                for rank in cls.RANKS
                ]

    def __init__(self, rank: str, suit: str) -> None:
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank. Rank must be one of the following: {self.RANKS}")
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit. Suit must be one of the following: {self.SUITS}")
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        """The rank property."""
        return self._rank
    @rank.setter
    def rank(self, value):
        if value.rank not in Card.RANKS:
            raise ValueError(f"Invalid rank. Rank must be one of the following: {self.RANKS}")
        if value.suit not in Card.SUITS:
            raise ValueError(f"Invalid suit. Suit must be one of the following: {self.SUITS}")
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

    def __eq__(self, __value: object) -> bool:
        return all([self.rank == __value.rank, self.suit == __value.suit])

    def __lt__(self, __value: object) -> bool:
        current_card_index = self.RANKS.index(self.rank)
        other_card_rank_index = self.RANKS.index(__value.rank)
        return current_card_index < other_card_rank_index
    
