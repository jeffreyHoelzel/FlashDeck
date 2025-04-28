from application.ports.quiz_repository import QuizRepository
from domain.quiz import Quiz
from domain.deck import Deck
from domain.card import Card

class CreateQuizService:
    def __init__(self, quiz_repo: QuizRepository):
        self.quiz_repo = quiz_repo

    def execute(self, name: str, decks_data: list[dict]) -> None:
        if self.quiz_repo.get_by_name(name):
            raise ValueError(f"Quiz with name '{name}' already exists.")

        decks = []
        for deck_data in decks_data:
            cards = [Card(card["question"], card["answer"]) for card in deck_data["cards"]]
            deck = Deck(name=deck_data["name"], cards=cards)
            decks.append(deck)

        new_quiz = Quiz(name=name, decks=decks)
        self.quiz_repo.save(new_quiz)
