class Deck(object):
    def __init__(self) -> None:
        self.cards = []
    
    def add_cards(self, cards: list) -> None:
        self.cards.extend(cards)
