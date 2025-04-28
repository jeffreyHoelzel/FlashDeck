from application.ports.quiz_repository import QuizRepository
from domain.quiz import Quiz
from .sqlalchemy_quiz_model import QuizModel
from .mappers import quiz_model_to_domain, quiz_domain_to_model
from .database import db

class SQLAlchemyQuizRepository(QuizRepository):

    def get_by_name(self, name: str) -> Quiz | None:
        model = QuizModel.query.filter_by(name=name).first()
        return quiz_model_to_domain(model) if model else None

    def save(self, quiz: Quiz) -> None:
        existing_model = QuizModel.query.filter_by(name=quiz.name).first()
        if existing_model:
            db.session.delete(existing_model)
        model = quiz_domain_to_model(quiz)
        db.session.add(model)
        db.session.commit()

    def delete(self, name: str) -> None:
        model = QuizModel.query.filter_by(name=name).first()
        if model:
            db.session.delete(model)
            db.session.commit()

    def list_all(self) -> list[Quiz]:
        models = QuizModel.query.all()
        return [quiz_model_to_domain(m) for m in models]
