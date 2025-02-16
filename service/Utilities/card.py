from .database import db
from sqlalchemy.orm import relationship
# TODO: finish db set-up using sqlalchemy

class Card(db.Model):
    __tablename__ = "cards"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    deck_id = db.Column(db.Integer, db.ForeignKey("decks.id"))

    deck = relationship("Deck", back_populates="cards")

    def __init__(self, question, answer, deck_id):
        self.question = question
        self.answer = answer
        self.deck_id = deck_id

    def edit_question(self, new_question):
        self.question = new_question

    def edit_answer(self, new_answer):
        self.answer = new_answer
