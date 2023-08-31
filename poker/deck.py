class Deck(object):
    def __init__(self) -> None:
        self.cards = []
    
    def add_cards(self, cards: list) -> None:
        self.cards.extend(cards)

    def create_cards(self, cards) -> None:
        cards = []
        self.add_cards(cards)

