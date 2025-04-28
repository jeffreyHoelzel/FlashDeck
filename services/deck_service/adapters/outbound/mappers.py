from domain.deck import Deck
from domain.card import Card
from domain.quiz import Quiz

from .sqlalchemy_deck_model import DeckModel
from .sqlalchemy_card_model import CardModel
from .sqlalchemy_quiz_model import QuizModel
from .quiz_deck_relationship import quiz_deck_relationship

def card_model_to_domain(card_model: CardModel) -> Card:
    return Card(
        question=card_model.question,
        answer=card_model.answer
    )

def card_domain_to_model(card: Card, deck_id=None) -> CardModel:
    return CardModel(
        question=card.question,
        answer=card.answer,
        deck_id=deck_id
    )

def deck_model_to_domain(deck_model: DeckModel) -> Deck:
    cards = [card_model_to_domain(c) for c in deck_model.cards]
    return Deck(
        name=deck_model.name,
        cards=cards
    )

def deck_domain_to_model(deck: Deck) -> DeckModel:
    model = DeckModel(name=deck.name)
    model.cards = [card_domain_to_model(card) for card in deck.cards]
    return model

def quiz_model_to_domain(quiz_model: QuizModel) -> Quiz:
    decks = [deck_model_to_domain(d) for d in quiz_model.decks]
    return Quiz(
        name=quiz_model.name,
        decks=decks
    )

def quiz_domain_to_model(quiz: Quiz) -> QuizModel:
    model = QuizModel(name=quiz.name)
    model.decks = [deck_domain_to_model(deck) for deck in quiz.decks]
    return model
