from .database import db
from sqlalchemy.orm import relationship
from .quiz_deck_relationship import quiz_deck_relationship

class Quiz(db.Model):
    __tablename__ = "quizzes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)

    decks = relationship("Deck", secondary=quiz_deck_relationship, back_populates="quizzes", cascade="all, delete")

    def __init__(self, name, decks=None):
        self.name = name
        if decks:
            self.decks = decks
    
    def change_name(self, new_name):
        self.name = new_name

    def add_deck(self, new_deck):
        self.decks.append(new_deck)

    def remove_deck(self, deck_to_remove):
        self.decks.remove(deck_to_remove)
