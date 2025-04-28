class Card:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def edit_question(self, new_question):
        self.question = new_question

    def edit_answer(self, new_answer):
        self.answer = new_answer
