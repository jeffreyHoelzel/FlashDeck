import random
from models.deck import Deck


def start_quiz(deck_id):
    deck = Deck.query.get(deck_id)

    if not deck:
        return "Deck not found"

    flashcards = [{"id": card.id, "question": card.question, "answer": card.answer} for card in deck.cards]

    if not flashcards:
        return "Flashcards not found"

    random.shuffle(flashcards)

    return {"deck_id": deck.id, "deck_name": deck.name, "flashcards": flashcards}