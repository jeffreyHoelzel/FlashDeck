class Card:
    def __init__(self, question, answer):
        self._question = question
        self._answer = answer
    
    @property
    def question(self):
        return self._question
    
    @property
    def answer(self):
        return self._answer

    def edit_question(self, new_question):
        self._question = new_question

    def edit_answer(self, new_answer):
        self._answer = new_answer
