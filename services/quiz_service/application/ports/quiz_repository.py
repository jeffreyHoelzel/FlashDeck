from abc import ABC, abstractmethod
from domain.quiz import Quiz

class QuizRepository(ABC):

    @abstractmethod
    def get_by_name(self, name: str) -> Quiz:
        pass

    @abstractmethod
    def save(self, quiz: Quiz) -> None:
        pass

    @abstractmethod
    def delete(self, name: str) -> None:
        pass

    @abstractmethod
    def list_all(self) -> list[Quiz]:
        pass
