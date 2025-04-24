from repositories.deck_repo import *
from repositories.card_repo import *

def create_deck_service(name, cards):
    # Check if a deck with the same name already exists
    existing_deck = Deck.query.filter_by(name=name).first()
    if existing_deck:
        return None

    # Create a new deck
    new_deck = Deck(name=name)
    db.session.add(new_deck)
    db.session.commit()

    for card_data in cards:
        question = card_data.get("question")
        answer = card_data.get("answer")
        if question and answer:
            new_card = Card(question=question, answer=answer, deck_id=new_deck.id)
            db.session.add(new_card)

    db.session.commit()
    return new_deck

def edit_deck_service(deck_id, name="", cards=None):
    deck = Deck.query.get(deck_id)
    if not deck:
        return None

    if name:
        deck.name = name

    if cards:
        for card_data in cards:
            card_id = card_data.get("id")
            question = card_data.get("question")
            answer = card_data.get("answer")

            if card_id:
                existing_card = Card.query.get(card_id)
                if existing_card:
                    existing_card.question = question
                    existing_card.answer = answer
            else:
                new_card = Card(question=question, answer=answer, deck_id=deck.id)
                db.session.add(new_card)

    db.session.commit()
    return deck

def delete_deck_service(deck_id):
    try:
        deck = Deck.query.get(deck_id)

        if not deck:
            return "No deck found"
        
        db.session.delete(deck)
        db.session.commit()
    
    except Exception as e:
        db.session.rollback()
        print(f"Error deleting deck: {e}")
        return "Error deleting deck"
    
def get_all_decks_service():
    decks = Deck.query.all()
    deck_list = [{"id": deck.id, "name": deck.name} for deck in decks]

    return deck_list

def get_deck_service(deck_id):
    deck = Deck.query.get(deck_id)

    if not deck:
        return None

    cards = [{"id": card.id, "question": card.question, "answer": card.answer} for card in deck.cards]

    return {"id": deck.id, "name": deck.name, "cards": cards}
