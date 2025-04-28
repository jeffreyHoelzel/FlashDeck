from application.ports.deck_repository import DeckRepository
from domain.deck import Deck
from .sqlalchemy_deck_model import DeckModel
from .mappers import deck_model_to_domain, deck_domain_to_model
from .database import db

class SQLAlchemyDeckRepository(DeckRepository):
    
    def get_by_name(self, name: str) -> Deck | None:
        model = DeckModel.query.filter_by(name=name).first()
        return deck_model_to_domain(model) if model else None

    def save(self, deck: Deck) -> None:
        existing_model = DeckModel.query.filter_by(name=deck.name).first()
        if existing_model:
            db.session.delete(existing_model)
        model = deck_domain_to_model(deck)
        db.session.add(model)
        db.session.commit()

    def delete(self, name: str) -> None:
        model = DeckModel.query.filter_by(name=name).first()
        if model:
            db.session.delete(model)
            db.session.commit()

    def list_all(self) -> list[Deck]:
        models = DeckModel.query.all()
        return [deck_model_to_domain(m) for m in models]
