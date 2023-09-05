from poker.validators import Validator

class StraightValidator(Validator):
    def __init__(self, cards) -> None:
        super().__init__(cards)
        self._name = "Straight"
        self._batch_of_straight_cards = self._get_batch_of_straightcards()

    def is_valid(self) -> bool:
        if len(self.cards) < 5:
            return False
        return len(self.batch_of_straight_cards) >= 1

    def valid_cards(self) -> list:
        return self.batch_of_straight_cards[-1]

    def _every_element_increasing_by_1(self, rank_indexes) -> bool:
        for index in range(4):
            if rank_indexes[index + 1] - rank_indexes[index] != 1:
                return False
        return True

    @property
    def batch_of_straight_cards(self):
        """The batch_of_straight_cards property."""
        return self._batch_of_straight_cards
    @batch_of_straight_cards.setter
    def batch_of_straight_cards(self, value):
        self._batch_of_straight_cards = value

    def _get_batch_of_straightcards(self):
        index = 0
        final_index = len(self.cards) - 1
        collections_of_five_straight_cards_in_a_row = []
        while index + 4 <= final_index:
            next_five_cards = self.cards[index: index + 5]
            next_five_rank_indices = [card.rank_index for card in next_five_cards]
            if self._every_element_increasing_by_1(next_five_rank_indices):
                collections_of_five_straight_cards_in_a_row.append(next_five_cards)
            index += 1
        return collections_of_five_straight_cards_in_a_row 

