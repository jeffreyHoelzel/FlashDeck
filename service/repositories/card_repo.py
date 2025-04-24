from models.card import Card
from database import db

def get_all_cards():
    return Card.query.all()

def get_card_by_id(card_id):
    return Card.query.get(card_id)

def create_card(question, answer, deck_id):
    card = Card(question, answer, deck_id)
    db.session.add(card)
    db.session.commit()
    return card

def delete_card(card):
    db.session.delete(card)
    db.session.commit()
