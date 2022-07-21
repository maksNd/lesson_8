import json
import random
from question import Question

question_file = r'questions.json'


def get_list_with_questions_from_file(filename=r'questions.json') -> list:
    """
    Формирует список вопросов (экземпляров класса Question) из файла
    :param filename:
    :return list:
    """
    list_with_questions = []
    with open(filename) as file:
        for i in json.loads(file.read()):
            list_with_questions.append(Question(**i))
            random.shuffle(list_with_questions)

    return list_with_questions


def get_statistic(user_points: int, right_answer_counter: int, questions_quantity: int) -> str:
    """
    Возвращает статистику на основе данных ответов пользователя
    :param user_points:
    :param right_answer_counter:
    :param questions_quantity:
    :return str:
    """
    return f"Вот и все!".rjust(40) + "\n" + \
           f"Отвечено {right_answer_counter} вопроса из {questions_quantity}".rjust(40) + "\n" + \
           f"Набрано баллов: {user_points}".rjust(40)
