class Deck:
    def __init__(self, name, decks=[]):
        self._name = name
        self._decks = decks

    @property
    def name(self):
        return self._name
    
    @property
    def decks(self):
        return self._decks
    
    def change_name(self, new_name):
        self._name = new_name

    def add_deck(self, new_deck):
        self._decks.append(new_deck)

    def remove_deck(self, deck_to_remove):
        self._decks.remove(deck_to_remove)
