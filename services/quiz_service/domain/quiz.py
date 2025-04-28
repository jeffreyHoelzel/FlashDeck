class Quiz:
    def __init__(self, name, decks=None):
        self.name = name
        self.decks = decks if decks else []

    def change_name(self, new_name):
        self.name = new_name

    def add_deck(self, new_deck):
        self.decks.append(new_deck)

    def remove_deck(self, deck_to_remove):
        self.decks.remove(deck_to_remove)
