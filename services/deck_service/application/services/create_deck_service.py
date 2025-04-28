from application.ports.deck_repository import DeckRepository
from domain.deck import Deck
from domain.card import Card

class CreateDeckService:
    def __init__(self, deck_repo: DeckRepository):
        self.deck_repo = deck_repo

    def execute(self, name: str, cards_data: list[dict]) -> None:
        if self.deck_repo.get_by_name(name):
            raise ValueError(f"Deck with name '{name}' already exists.")
        
        cards = [Card(card["question"], card["answer"]) for card in cards_data]
        new_deck = Deck(name=name, cards=cards)
        self.deck_repo.save(new_deck)
