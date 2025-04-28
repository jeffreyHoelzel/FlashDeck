class Deck:
    def __init__(self, name, cards=None):
        self.name = name
        self.cards = cards if cards else []

    def change_name(self, new_name):
        self.name = new_name

    def add_card(self, new_card):
        self.cards.append(new_card)

    def remove_card(self, card_to_remove):
        self.cards.remove(card_to_remove)
