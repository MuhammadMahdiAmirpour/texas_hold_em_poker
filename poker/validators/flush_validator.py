from poker.validators import Validator

class FlushValidator(Validator):
    def __init__(self, cards) -> None:
        super().__init__(cards)
        self._name = "Flush"

    def is_valid(self) -> bool:
        suits_that_occur_5_or_more_times = {
                suit: suit_count
                for suit, suit_count in self._card_suit_counts.items()
                if suit_count >= 5
                }
        return len(suits_that_occur_5_or_more_times) == 1

    def valid_cards(self) -> list:
        cards = [
                card 
                for card in self.cards 
                if card.suit in self._suits_that_occur_five_or_more_times.keys()]
        return cards[-5:]
    @property
    def _card_suit_counts(self):
        card_suit_counts = {}
        for card in self.cards:
            card_suit_counts.setdefault(card.suit, 0)
            card_suit_counts[card.suit] += 1
        return card_suit_counts

    @property
    def _suits_that_occur_five_or_more_times(self):
        return {
                    suit: suit_count
                    for suit, suit_count in self._card_suit_counts.items()
                    if suit_count >= 5
                }


