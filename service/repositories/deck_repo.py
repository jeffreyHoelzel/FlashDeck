from models.deck import Deck
from database import db

def get_all_decks():
    return Deck.query.all()

def get_deck_by_id(deck_id):
    return Deck.query.get(deck_id)

def create_deck(name):
    deck = Deck(name)
    db.session.add(deck)
    db.session.commit()
    return deck

def delete_deck(deck):
    db.session.delete(deck)
    db.session.commit()
