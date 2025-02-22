from .database import db

"""
    Table designed to handle the relationship between quizzes and decks.
"""
quiz_deck_relationship = db.Table(
    "quiz_deck_relationship", db.metadata, 
    db.Column("quiz_id", db.Integer, db.ForeignKey("quizzes.id"), primary_key=True), 
    db.Column("deck_id", db.Integer, db.ForeignKey("decks.id"), primary_key=True)
)
