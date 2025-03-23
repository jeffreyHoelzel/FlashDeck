from .database import db

quiz_deck_relationship = db.Table(
    "quiz_deck_relationship", db.metadata, 
    db.Column("quiz_id", db.Integer, db.ForeignKey("quizzes.id"), primary_key=True), 
    db.Column("deck_id", db.Integer, db.ForeignKey("decks.id"), primary_key=True)
)
