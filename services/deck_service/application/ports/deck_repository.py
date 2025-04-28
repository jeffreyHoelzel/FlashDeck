from abc import ABC, abstractmethod
from domain.deck import Deck

class DeckRepository(ABC):
    
    @abstractmethod
    def get_by_name(self, name: str) -> Deck:
        pass

    @abstractmethod
    def save(self, deck: Deck) -> None:
        pass

    @abstractmethod
    def delete(self, name: str) -> None:
        pass

    @abstractmethod
    def list_all(self) -> list[Deck]:
        pass
