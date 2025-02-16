from .database import db
from sqlalchemy.orm import relationship
from .quiz_deck_relationship import quiz_deck_relationship

class Deck(db.Model):
    __tablename__ = "decks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)

    cards = relationship("Card", back_populates="deck", cascade="all, delete")
    quizzes = relationship("Quiz", secondary=quiz_deck_relationship, back_populates="decks", cascade="all, delete")

    def __init__(self, name, cards=None):
        self.name = name
        if cards:
            self.cards = cards
    
    def change_name(self, new_name):
        self.name = new_name

    def add_card(self, new_card):
        self.cards.append(new_card)

    def remove_card(self, card_to_remove):
        self.cards.remove(card_to_remove)
