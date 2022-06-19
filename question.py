class Question:

    def __init__(self, q, d, a):
        self.question_text = q
        self.difficulty = d
        self.right_answer = a

        self.is_question = False
        self.user_answer = None
        self.points = int(self.difficulty) * 10

    def __repr__(self):
        return f"({self.question_text[:15]}...Question)"

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.points

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        # self.user_answer = user_answer
        return self.user_answer == self.right_answer

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f"{self.question_text}\nСложность {self.difficulty}/5"

    def build_feedback(self):
        if self.is_correct():
        # if self.user_answer == self.right_answer:
            return f"Ответ верный, получено {self.points} баллов"
        else: return f"Ответ неверный, верный ответ {self.right_answer}"
