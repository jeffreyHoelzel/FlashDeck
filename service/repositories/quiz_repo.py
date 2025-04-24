from models.quiz import Quiz
from database import db

def get_all_quizzes():
    return Quiz.query.all()

def get_quiz_by_id(quiz_id):
    return Quiz.query.get(quiz_id)

def create_quiz(name, decks=None):
    if decks:
        quiz = Quiz(name, decks=decks)
    else:
        quiz= Quiz(name)
    
    db.session.add(quiz)
    db.session.commit()
    return quiz

def delete_quiz(quiz):
    db.session.delete(quiz)
    db.session.commit()