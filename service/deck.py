class Deck:
    def __init__(self, name, cards=[]):
        self._name = name
        self._cards = cards
    
    @property
    def name(self):
        return self._name
    
    @property
    def cards(self):
        return self._cards
    
    def change_name(self, new_name):
        self._name = new_name

    def add_card(self, new_card):
        self._cards.append(new_card)

    def remove_card(self, card_to_remove):
        self._cards.remove(card_to_remove)
